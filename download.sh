#!/bin/bash

echo "Downloading the model weights for animal faces ..."
URL=https://github.com/fpaupier/stargan-v2/releases/download/v1.0/100000_nets_ema.ckpt
mkdir -p ./expr/checkpoints
OUT_FILE=./expr/checkpoints/100000_nets_ema.ckpt
wget -N $URL -O $OUT_FILE
echo "Download complete! Model weights available at ./expr/checkpoints/100000_nets_ema.ckpt"
