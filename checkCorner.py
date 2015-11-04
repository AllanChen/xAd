__author__ = 'Allan'
import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

img3 = cap.read()

img = cv2.imread('/Users/Allan/Desktop/xAd_Resource/gameboy-query.jpg',0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img3,None)

# compute the descriptors with ORB
kp, des = orb.compute(img3, kp)

# draw only keypoints location,not size and orientation

# img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)

img2 = cv2.drawKeypoints(img3,kp,img3,color=(0,255,0),flags=0)

#plt.imshow(img2),plt.show()