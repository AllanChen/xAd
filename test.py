__author__ = 'Allan'

import numpy as np
import cv2

green = np.uint8([[[48,66,76]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green