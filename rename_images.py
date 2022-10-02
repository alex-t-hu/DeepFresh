import os
import shutil

path = 'C:\\Users\\Risha\\Downloads\\dataset'
trainpath = os.path.join(path, 'train')
testpath = os.path.join(path, 'test')

for dirname in os.listdir(trainpath):
    for imname in os.listdir(os.path.join(trainpath, dirname)):
        os.rename(os.path.join(trainpath, dirname, imname), os.path.join(trainpath, dirname, dirname+imname))

for dirname in os.listdir(testpath):
    for imname in os.listdir(os.path.join(testpath, dirname)):
        os.rename(os.path.join(testpath, dirname, imname), os.path.join(testpath, dirname, dirname+imname))