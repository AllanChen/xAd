__author__ = 'Allan'
import sys
sys.path.append('/usr/local/lib')
import numpy as np
import cv2

img = cv2.imread("/Users/Allan/Desktop/tao.jpg")
video = cv2.VideoCapture("/Users/Allan/Desktop/1.mp4")

while(1):
    ret ,frame = video.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()