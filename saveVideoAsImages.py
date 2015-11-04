__author__ = 'Allan'
import sys
sys.path.append('/Users/Allan/Desktop/opencv-3.0.0/build/lib')
import numpy as np
import cv2

camera = cv2.VideoCapture(0)
i = 0
while True:
   f,img = camera.read()
   cv2.imshow("webcam",img)
   if (cv2.waitKey(5) != -1):
       break
   cv2.imwrite('{0:05d}.jpg'.format(i),img)
   i += 1