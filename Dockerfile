FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt install && apt install software-properties-common -y
RUN apt-get install python3.8 python3-pip -y
RUN apt-get install -y python-dev
RUN apt-get install gfortran libopenblas-dev liblapack-dev -y

# OpenCV requirements
RUN python3.8 -m pip install --upgrade pip
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx

WORKDIR /usr/app
COPY ./requirements.txt requirements.txt
COPY ./expr/checkpoints/100000_nets_ema.ckpt expr/checkpoints/100000_nets_ema.ckpt
COPY ./core/ core/
COPY ./main.py main.py

RUN --mount=type=cache,target=/root/.cache/pip python3.8 -m pip install -r requirements.txt
