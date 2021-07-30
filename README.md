
## StarGAN v2

Image synthesis in Python - a light version for inference.

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

**AFHQ.** To download the pre-trained network, run the following commands:
```bash
bash download.sh 
```


## Generating interpolation videos
After downloading the pre-trained networks, you can synthesize output images reflecting diverse styles of reference images.
The following commands will save generated images and interpolation videos to the `expr/results` directory. 


**AFHQ.** To generate images, run the following command:
```bash
python main.py 
```
You can adjust the different inference options in the [`config.yaml`](./config.yaml).

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

