#!/bin/bash

#sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-magic

pip3 install -U augly
pip3 install -r requirements.txt

unzip unzip_me.zip
rm unzip_me.zip
