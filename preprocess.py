import os
import shutil
import cv2

path = 'C:\\Users\\Risha\\Downloads\\dataset'
def deriveDataset():
    os.chdir(path)

    os.chdir(os.path.join(os.getcwd(), 'train'))

    for i in range(3, 9):
        reg = os.listdir()[i]
        reg1 = os.listdir()[i + 9]
        fruit = os.listdir()[i][2:].lower()
        print(fruit)
        os.mkdir(os.path.join(os.getcwd(), 'fresh' + fruit))
        os.mkdir(os.path.join(os.getcwd(), 'rotten' + fruit))
        os.mkdir(os.path.join(path, 'test', 'fresh' + fruit))
        os.mkdir(os.path.join(path, 'test', 'rotten' + fruit))
        for j in range(1, 201):
            shutil.copy(os.path.join(os.getcwd(), reg, str(j) + '.jpg'), os.path.join(path, 'test', 'fresh' + fruit, str(j) + '.jpg'))
            shutil.copy(os.path.join(os.getcwd(), reg1, str(j) + '.jpg'), os.path.join(path, 'test', 'rotten' + fruit, str(j) + '.jpg'))
        for j in range(201, 1001):
            shutil.copy(os.path.join(os.getcwd(), reg, str(j) + '.jpg'), os.path.join(path, 'train', 'fresh' + fruit, str(j) + '.jpg'))
            shutil.copy(os.path.join(os.getcwd(), reg1, str(j) + '.jpg'), os.path.join(path, 'train', 'rotten' + fruit, str(j) + '.jpg'))

        shutil.rmtree(os.path.join(os.getcwd(), reg))
        shutil.rmtree(os.path.join(os.getcwd(), reg1))\

def resizeImages():
    trainpath = os.path.join(path, 'train')
    testpath = os.path.join(path, 'test')
    for dir in os.listdir(trainpath):
        for filename in os.listdir(os.path.join(trainpath, dir)):
            img = cv2.imread(os.path.join(trainpath, dir, filename))
            img = cv2.resize(img, (224, 224))
            cv2.imwrite(os.path.join(trainpath, dir, filename), img)

    for dir in os.listdir(testpath):
        for filename in os.listdir(os.path.join(testpath,dir)):
            img = cv2.imread(os.path.join(testpath, dir, filename))
            img = cv2.resize(img, (224, 224))
            cv2.imwrite(os.path.join(testpath, dir, filename), img)

deriveDataset()
resizeImages()

