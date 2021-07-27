
## StarGAN v2 for inference

Image synthesis in Python - a dockerized version.

## Style transformation
Style transfer on animal images.

![](assets/afhq_interpolation.gif)


## Getting started
Clone this repository:

```bash
git clone git@github.com:fpaupier/stargan-v2.git
cd stargan-v2/
```

Install the dependencies, python 3.7:
```bash
python3 -m venv .venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Datasets and pre-trained networks
We provide a script to download datasets used in StarGAN v2 and the corresponding pre-trained networks. The datasets and network checkpoints will be downloaded and stored in the `data` and `expr/checkpoints` directories, respectively.

**AFHQ.** To download the [AFHQ](https://github.com/clovaai/stargan-v2/blob/master/README.md#animal-faces-hq-dataset-afhq) dataset and the pre-trained network, run the following commands:
```bash
bash download.sh afhq-v2-dataset
bash download.sh pretrained-network-afhq
```


## Generating interpolation videos
After downloading the pre-trained networks, you can synthesize output images reflecting diverse styles (e.g., hairstyle) of reference images. The following commands will save generated images and interpolation videos to the `expr/results` directory. 


To transform a custom image, first crop the image manually so that the proportion of face occupied in the whole is similar to that of CelebA-HQ. Then, run the following command for additional fine rotation and cropping. All custom images in the `inp_dir` directory will be aligned and stored in the `out_dir` directory.

```bash
python main.py --mode align \
               --inp_dir assets/representative/custom/dog \
               --out_dir assets/representative/afhq/src/dog
```


**AFHQ.** To generate images and interpolation videos, run the following command:
```bash
python main.py --num_domains 3 --resume_iter 100000 --w_hpf 0 \
               --checkpoint_dir expr/checkpoints/afhq \
               --result_dir expr/results/afhq \
               --src_dir assets/representative/afhq/src \
               --ref_dir assets/representative/afhq/ref
```

--------

### Acknowledgements
This work is based on the following repo https://github.com/clovaai/stargan-v2 and its associated paper:

```
@inproceedings{choi2020starganv2,
  title={StarGAN v2: Diverse Image Synthesis for Multiple Domains},
  author={Yunjey Choi and Youngjung Uh and Jaejun Yoo and Jung-Woo Ha},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2020}
}
```

