__author__ = 'Allan'
import cv2
import numpy as np
class create_video_and_images:

    count_with_images = 0

    def create_images_from_video(self):
        print(1)

    def create_video_from_images(self):
        '''
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5 )
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)

    foucc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    videoWrite = cv2.VideoWriter("./videoImages/video_3.avi", foucc, 20.0, (width, height))

    for i in range(0, count_with_images):
        imageName = "/Users/Allan/Desktop/xAd/videoImages/%s.jpg" % str(i)
        saveCap = cv2.VideoCapture(imageName)
        ret, frame = saveCap.read()

        if ret:
            videoWrite.write(frame)
        else:
            print("can not save this image")
            break
            '''
