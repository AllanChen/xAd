__author__ = 'Allan'

import numpy as np
import cv2

img = cv2.imread('/Users/Allan/Desktop/xAd_Resource/12.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=30,param2=40,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    print(1)
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

#cv2.imshow('detected circles',cimg)
cv2.imwrite("/Users/Allan/Desktop/1.png",cimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()