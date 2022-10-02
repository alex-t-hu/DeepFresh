import cv2
import numpy as np
import glob
import shutil
import os
path = 'C:\\Users\\Risha\\Downloads\\dataset'
trainpath = 'C:\\Users\\Risha\\Downloads\\dataset\\train'
testpath = 'C:\\Users\\Risha\\Downloads\\dataset\\test'
# get bounding box from images by using OpenCV
def get_imgage_range(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower = np.array([0, 0, 0], dtype = "uint8")
  upper = np.array([255, 50, 255], dtype = "uint8")
  img = cv2.inRange(img, lower, upper)
  img = cv2.blur(img, (2, 2))
  ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
  img = cv2.bitwise_not(img)
  contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  contours = max(contours, key=lambda x: cv2.contourArea(x))
  #get bounding box posotion
  xmin, ymin, xmax, ymax = cv2.boundingRect(contours)
  #get the original width,height of the image
  dimensions = img.shape
  h = img.shape[0]
  w = img.shape[1]
  
  #to calculate the bndBox info of this image for yolo
  xp = (xmin + (xmax-xmin)/2) * 1.0 / w
  yp = (ymin + (ymax-ymin)/2) * 1.0 / h
  wp = (xmax-xmin) * 1.0 / w
  hp = (ymax-ymin) * 1.0 / h
  return xp, yp, wp, hp

def create_yolotrain():
    out_train = os.path.join(path, 'yolotrain')
    if not os.path.exists(out_train):
        os.mkdir(out_train)
    # go through the dataset folder, and find out all png file
    for dirname in os.listdir(trainpath):
        # define the output folder
        output = os.path.join(out_train, dirname)
        # to check if the output folder exists, or create it
        if not os.path.exists(output):
            os.mkdir(output)
            os.mkdir(output + "label")
        print(dirname)
        for imgdir in os.listdir(os.path.join(trainpath, dirname)):
            
            # define the output path of images and bndBox label files
            out_img_path=os.path.join(output, imgdir)
            out_lbl_text = os.path.join(output + "label", imgdir)
            out_lbl_text= out_lbl_text.replace('.jpg', '.txt')
            out_lbl_text = out_lbl_text.replace('.png', '.txt')
            
            #define class for images
            label=0
            if dirname == 'freshapples':
                label=0
            elif dirname == 'freshbanana':
                label=1
            elif dirname == 'freshlemon':
                label=2
            elif dirname == 'freshlulo':
                label = 3
            elif dirname == 'freshmango':
                label = 4
            elif dirname == 'freshoranges':
                label = 5
            elif dirname == 'freshstrawberry':
                label = 6
            elif dirname == 'freshtamarillo':
                label = 7
            elif dirname == 'freshtomato':
                label = 8
            elif dirname == 'rottenapples':
                label=9
            elif dirname == 'rottenbanana':
                label=10
            elif dirname == 'rottenlemon':
                label=11
            elif dirname == 'rottenlulo':
                label = 12
            elif dirname == 'rottenmango':
                label = 13
            elif dirname == 'rottenoranges':
                label = 14
            elif dirname == 'rottenstrawberry':
                label = 15
            elif dirname == 'rottentamarillo':
                label = 16
            elif dirname == 'rottentomato':
                label = 17
            
            img_path = os.path.join(trainpath, dirname, imgdir)
            #to generate image's yolo label
            if os.path.exists(img_path):
                #get yolo label
                xmin, ymin, xmax, ymax=get_imgage_range(img_path)
                #to save yolo label
                with open(out_lbl_text, 'w') as f:
                    f.write('%s %s %s %s %s\n' % (label,xmin, ymin, xmax, ymax))
                # copy image file to output
                shutil.copyfile(img_path, out_img_path)

def create_yolotest():
    out_test = os.path.join(path, 'yolotest')
    if not os.path.exists(out_test):
        os.mkdir(out_test)
    # go through the dataset folder, and find out all png file
    for dirname in os.listdir(testpath):
        # define the output folder
        output = os.path.join(out_test, dirname)
        # to check if the output folder exists, or create it
        if not os.path.exists(output):
            os.mkdir(output)
            os.mkdir(output + "label")
        print(dirname)
        for imgdir in os.listdir(os.path.join(testpath, dirname)):
            
            # define the output path of images and bndBox label files
            out_img_path=os.path.join(output, imgdir)
            out_lbl_text = os.path.join(output + "label", imgdir)
            out_lbl_text= out_lbl_text.replace('.jpg', '.txt')
            out_lbl_text = out_lbl_text.replace('.png', '.txt')
            
            #define class for images
            label=0
            if dirname == 'freshapples':
                label=0
            elif dirname == 'freshbanana':
                label=1
            elif dirname == 'freshlemon':
                label=2
            elif dirname == 'freshlulo':
                label = 3
            elif dirname == 'freshmango':
                label = 4
            elif dirname == 'freshoranges':
                label = 5
            elif dirname == 'freshstrawberry':
                label = 6
            elif dirname == 'freshtamarillo':
                label = 7
            elif dirname == 'freshtomato':
                label = 8
            elif dirname == 'rottenapples':
                label=9
            elif dirname == 'rottenbanana':
                label=10
            elif dirname == 'rottenlemon':
                label=11
            elif dirname == 'rottenlulo':
                label = 12
            elif dirname == 'rottenmango':
                label = 13
            elif dirname == 'rottenoranges':
                label = 14
            elif dirname == 'rottenstrawberry':
                label = 15
            elif dirname == 'rottentamarillo':
                label = 16
            elif dirname == 'rottentomato':
                label = 17
            
            img_path = os.path.join(testpath, dirname, imgdir)
            #to generate image's yolo label
            if os.path.exists(img_path):
                #get yolo label
                xmin, ymin, xmax, ymax=get_imgage_range(img_path)
                #to save yolo label
                with open(out_lbl_text, 'w') as f:
                    f.write('%s %s %s %s %s\n' % (label,xmin, ymin, xmax, ymax))
                # copy image file to output
                shutil.copyfile(img_path, out_img_path)

#get_imgage_range(os.path.join(testpath, 'freshstrawberry', 'freshstrawberry6.jpg'))
create_yolotrain()
create_yolotest()