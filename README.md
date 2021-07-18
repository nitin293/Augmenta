# Augmenta

This is a image augmentation tool that uses `Augly` by `Facebook` for image augmentation. We have implemented a few filters from the library. This script takes `input image path` and `output image path` in order to automate the reading and writing processes of the images.

## Requirements

* The major requirement of the program is that, you'll need a `Linux` environment for running this file efficiently, since the `Augly` library is in its initial stage of development and is not been compitable with `Windows` environment for now.
* The second requirement is `Python3` and `pip3` installed in your system.
* The third requirement is `python3-magic` installed in your system.

## Uses

* Clone or download the github repository.
* Run the `run.sh` file to install and set up the required environment.
* Run the `augmenta.py` file.

Commands : 

```
sudo apt-get install git -y
git clone https://gitlab.com/nitin293/image-augmentation
cd image-augmentation
bash run.sh
```

`python3 aug_singlelayer.py`

`python3 aug_multilayer.py`
