# save_numpy_image
# https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/


import numpy as np
import cv2
import os

training_dataset = "training_data-2021-02-14-2"

l = os.listdir("training_data/"+training_dataset)
n = len(l)
 
os.mkdir("screenshots/"+training_dataset)

for k in range(n):
    training_data = np.load("training_data/"+training_dataset+"/training_data-"+str(k+1)+".npy",allow_pickle=True) 

    img_array = []

    os.mkdir("screenshots/"+training_dataset+"/screenshots"+str(k+1))

    for i in range(len(training_data)):
        # print(img[0][0])
        img_array.append(training_data[i][0])
        cv2.imwrite("screenshots/"+training_dataset+"/screenshots"+str(k+1)+"/training_data_"+str(i)+".jpg",training_data[i][0])
