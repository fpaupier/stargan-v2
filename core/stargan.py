"""
StarGAN v2
Copyright (c) 2020-present NAVER Corp.

This work is licensed under the Creative Commons Attribution-NonCommercial
4.0 International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""

import os
from os.path import join as ospj
import time
import datetime
from munch import Munch

import torch
import torch.nn as nn
import torch.nn.functional as F

from core.model import build_model
from core.checkpoint import CheckpointIO
from core.data_loader import InputFetcher
import core.utils as utils


class Stargan(nn.Module):
    def __init__(self, args: dict):
        super().__init__()
        self.args = args
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.nets, self.nets_ema = build_model(args)
        # below setattrs are to make networks be children of Stargan, e.g., for self.to(self.device)
        for name, module in self.nets.items():
            utils.print_network(module, name)
            setattr(self, name, module)
        for name, module in self.nets_ema.items():
            setattr(self, name + '_ema', module)

        self.ckptios = [CheckpointIO(ospj(args['checkpoint_dir'], '{:06d}_nets_ema.ckpt'), data_parallel=True, **self.nets_ema)]

        self.to(self.device)
        for name, network in self.named_children():
            # Do not initialize the FAN parameters
            if ('ema' not in name) and ('fan' not in name):
                print('Initializing %s...' % name)
                network.apply(utils.he_init)

    def _load_checkpoint(self, step):
        for ckptio in self.ckptios:
            ckptio.load(step)

    @torch.no_grad()
    def sample(self, loaders):
        nets_ema = self.nets_ema
        os.makedirs(self.args['result_dir'], exist_ok=True)
        self._load_checkpoint(self.args['resume_iter'])

        src = next(InputFetcher(loaders.src, None, self.args['latent_dim'], 'test'))
        ref = next(InputFetcher(loaders.ref, None, self.args['latent_dim'], 'test'))

        fname = ospj(self.args['result_dir'], 'reference.jpg')
        print('Working on {}...'.format(fname))
        start = time.perf_counter()
        utils.translate_using_reference(nets_ema, self.args, src.x, ref.x, ref.y, fname)
        duration = time.perf_counter() - start
        print(f'Image generation finished. Took {duration:.2f} seconds')
