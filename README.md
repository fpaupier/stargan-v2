
## StarGAN v2

Image synthesis in Python - a light version for inference.

![](./assets/afhq_interpolation.gif)
_A dockerized version of [clovaai/stargan-v2](https://github.com/clovaai/stargan-v2) for inference_

## Getting started

Clone this repository:

```bash
git clone git@github.com:fpaupier/stargan-v2.git
cd stargan-v2/
```

### Inference with docker

You can run an inference with the dockerized version, simply run thee folloing command to get an image generated under
the `expr/results` folder:
```bash
docker-compose up
```

You can adjust the different inference options in the [`config.yaml`](./config.yaml).


### Pre-trained networks
I provide a script to download a pretrained StarGAN v2 network. 
The network checkpoints will be downloaded and stored in the `expr/checkpoints` directory.

To download the network trained on animal faces, run the following commands:
```bash
bash download.sh 
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

