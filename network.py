import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import glob
import os
import numpy as np
import shutil
from PIL import Image

path = 'C:\\Users\\Risha\\Downloads\\dataset'

if not os.path.exists(os.path.join(path, 'data')):
    for folder in ['images', 'labels']:
        for split in ['train', 'val', 'test']:
            os.makedirs(os.path.join(path, 'data', folder, split))

yolotrainim = os.path.join(path, 'yolotrain', 'images')
yolotrainlabels = os.path.join(path, 'yolotrain', 'labels')
yolotestim = os.path.join(path, 'yolotest', 'images')
yolotestlabels = os.path.join(path, 'yolotest', 'labels')

for dirname in os.listdir(yolotrainim):
    i = 0
    for imname in os.listdir(os.path.join(yolotrainim, dirname)):
        labelname = imname.replace('.jpg', '.txt')
        labelname = labelname.replace('.png', '.txt')
        if i < 50:
            shutil.copyfile(os.path.join(yolotrainim, dirname, imname), os.path.join(path, 'data', 'images', 'val', imname))
            shutil.copyfile(os.path.join(yolotrainlabels, dirname + 'label', labelname), os.path.join(path, 'data', 'labels', 'val', labelname))
        else:
            shutil.copyfile(os.path.join(yolotrainim, dirname, imname), os.path.join(path, 'data', 'images', 'train', imname))
            shutil.copyfile(os.path.join(yolotrainlabels, dirname + 'label', labelname), os.path.join(path, 'data', 'labels', 'train', labelname))
        i += 1

for dirname in os.listdir(yolotestim):
    for imname in os.listdir(os.path.join(yolotestim, dirname)):
        labelname = imname.replace('.jpg', '.txt')
        labelname = labelname.replace('.png', '.txt')    
        shutil.copyfile(os.path.join(yolotestim, dirname, imname), os.path.join(path, 'data', 'images', 'test', imname))
        shutil.copyfile(os.path.join(yolotestlabels, dirname + 'label', labelname), os.path.join(path, 'data', 'labels', 'test', labelname))

