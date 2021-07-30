"""
StarGAN v2
Copyright (c) 2020-present NAVER Corp.

This work is licensed under the Creative Commons Attribution-NonCommercial
4.0 International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""

import os

from munch import Munch
from torch.backends import cudnn
import torch
import yaml

from core.data_loader import get_test_loader
from core.stargan import Stargan

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def subdirs(dname):
    return [d for d in os.listdir(dname)
            if os.path.isdir(os.path.join(dname, d))]


def main(args):
    print(args)
    torch.manual_seed(args['seed'])

    stargan = Stargan(args)

    assert len(subdirs(args['src_dir'])) == args['num_domains']
    assert len(subdirs(args['ref_dir'])) == args['num_domains']
    loaders = Munch(src=get_test_loader(root=args['src_dir'],
                                        img_size=args['img_size'],
                                        batch_size=args['val_batch_size'],
                                        shuffle=False,
                                        num_workers=args['num_workers']),
                    ref=get_test_loader(root=args['ref_dir'],
                                        img_size=args['img_size'],
                                        batch_size=args['val_batch_size'],
                                        shuffle=False,
                                        num_workers=args['num_workers']))
    stargan.sample(loaders)


if __name__ == '__main__':
    main(config)
