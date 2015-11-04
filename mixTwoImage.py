__author__ = 'Allan'
import cv2
import numpy as np
import globalSetting as gs
# Read images : src image will be cloned into dst

#cap  = cv2.VideoCapture(0)

im = cv2.imread("/Users/Allan/Desktop/xAd_Resource/bgbg.jpg")
obj= cv2.imread("/Users/Allan/Desktop/xAd_Resource/jiaduobao.png")

#bg = cap.read()

bg_img = cv2.imdecode(obj,0)

# Create an all white mask
#mask = 255 * np.ones(obj.shape, obj.dtype)

# The location of the center of the src in the dst
width, height, channels = im.shape
center = (height/2, width/2)

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, bg_img, obj, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, bg_img, obj, center, cv2.MIXED_CLONE)

# Write results
cv2.imwrite("/Users/Allan/Desktop/tao-normal-clone-example.jpg", normal_clone)
cv2.imwrite("/Users/Allan/Desktop/tao-mixed-clone-example.jpg", mixed_clone)
