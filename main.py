__author__ = 'Allan'
import sys
sys.path.append("/usr/local/lib")
import numpy as np
import cv2
import time

global video_path

video_path = "/Users/Allan/Desktop/cut.mp4"

camer_position_x = [130,94,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,90,90,90,90,90,90,91,91,92,92,93,93,94,95,96,96,96,97,98,99,100,101,101,102,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,121,123,123,124,125,126,127,128,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,144,145,146,147,148,149,150,150,150,151,152,152,152,152,153,154,155,155,155,156,157,158,158,158,158,158,159,160,161,162,162,162,162,162,162,162,162,162,163,163,163,163,163,163,162,161,158,158,158,157,156,155,154,152,151,151,150,149,149,148,148,147,146,145,144,143,142,141,141,140,139,139,138,137,136,135,134,133,132,131,131,130,130,129,129,128,127,126,125,124,123,123,122,121,121,120,119,118,118,117,117,116,115,114,113,113,112,111,111,110,109,109,108,107,106,105,104,103,102,101,100,100,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,78,77,76,75,75,75,75,74,73,72,71,70,69,68,68,67,67,66,66,65,65,64,63,62,61,61,60,60,59,58,57,57,57,57,56,55,54,53,53,52,52,51,50,50,49,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,47,47,47,48,49,50,51,52,53,54,55,56,56,57,58,58,59,60,60,61,62,63,64,65,65,66,67,68,69,70,71,71,72,73,74,75,75,76,77,78,79,80,81,82,83,84,85,85,86,87,88,88,89,90,91,91,91,91,92,92,92,92,92,92,92,92,93,93,94,95,96,97,98,99,100,101,102,102,102,102,102,102,103,104,105,106,107,108,109,110,111,112,112,113,113,114,115,116,117,117,117,117,117,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96,95, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94,93,92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 92,93, 94, 95, 95, 96, 96,97,98, 99, 99, 99, 100,101,102,103,104,105,106,106,107,108,108,109,110,112,113,114,114,114,115,116,117,117,118,119,119,120,120,120,121,122,123,124,125,126,126,126,126,126,126,126,127,128,129,130,131,132,133,134,135,136,137,137,137,138,139,140,141,141,142,142,143,144,144,145,146,147,148,149,150,151,151,151,152,153,153,153,154,155,156,156,156,156,156,156,157,158,158,158,158,159,159,159,159,159,159,160,160,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,161,160,160,159,158,158,158,158,158,158,158,157,156,155,155,155,154,153,152,151,150,149,149,148,147,146,145,144,143,142,141,140,139,138,138,137,136,136,136,136,135,134,133,133,133,133,133,132,131,131,130,129,128,127,126,125,124,123,121,120,119,118,117,117,116,115,114,113,113,112,111,110,109,108, 107,106,105,104,103,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,86,85,84,83,83,82,81,81,80,80,79,78,77,77,76,75,74,73,72,71,70,69,68,67,66,65,64,64,63,62,62,61,61,60,59,58,58,57,57,56,56,55,54,54,54,54,53,52,52,52,52,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51]
camer_position_y = [-22,-10,-10,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,0,1,2,3,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,1,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1,-1,0,0,0,-1,0,-1,0,-1,0,0,-1,-2,-1,0,0,0,-1,-1,0,-1,-1,-1,-1,-1,-2,-1,0,0,0,0,0,0,0,-1,-1,0,0,-1,-2,-1,0,-1,-2,-1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,-2,-3,-4,-5,-4,-3,-2,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def save_images_from_video(video_src):
    cap = cv2.VideoCapture(video_src)

    logo = cv2.imread("/Users/Allan/Desktop/tao.jpg")

    i = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow("saveVideoAsImage", frame)
        if ret:
            imageName = "%d.jpg" % i
            outPath = "./videoImages/%s" % imageName
            cv2.imwrite(outPath, frame)
            logo_position = (200,200)

            put_image_to_video(outPath, "/Users/Allan/Desktop/tao.jpg", outPath, logo_position)
        else:
            print("can not read frame Images")
        i += 1


def create_video_from_image(fristImage, num):
    cap = cv2.VideoCapture(fristImage)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5 )
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)

    foucc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    videoWrite = cv2.VideoWriter("./videoImages/video_3.avi", foucc, 20.0, (width, height))

    for i in range(0, num):
        imageName = "/Users/Allan/Desktop/xAd/videoImages/%s.jpg" % str(i)
        saveCap = cv2.VideoCapture(imageName)
        ret, frame = saveCap.read()

        if ret:
            videoWrite.write(frame)
        else:
            print("can not save this image")
            break

def set_tracker_position():
    cap = cv2.VideoCapture(video_path)
    # Read the first frame of the video
    ret, frame = cap.read()
    # Set the ROI (Region of Interest). Actually, this is a
    # rectangle of the building that we're tracking
    #c,r,w,h = 540, 340, 200,100
    c,r,w,h = 200, 100, 300,400
    #c,r,w,h = 200,100,200,00

    track_window = (c,r,w,h)
    # Create mask and normalized histogram
    roi = frame[r:r+h, c:c+w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    i=0
    while True:
        ret, frame = cap.read()
        if(ret):
             hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
             dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 10000)
             ret, track_window = cv2.meanShift(dst, track_window, term_crit)

             x,y,w,h = track_window
             #cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
             logo_position = (x,y,w,h)
             save_images(i, frame,logo_position)
             #cv2.imshow('Tracking', frame)
             #save_position_x(y)

             if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            create_video_from_image("/Users/Allan/Desktop/xAd/videoImages/0.jpg",i)
            break
        i +=1
    cap.release()
    cv2.destroyAllWindows()

def save_images(i, frame, position):
    imageName = "%d.jpg" % i
    outPath = "./videoImages/%s" % imageName
    cv2.imwrite(outPath, frame)
    put_image_to_video(outPath, "/Users/Allan/Desktop/tao.jpg", outPath, position)


def put_image_to_video(videoFramSrc, imageSrc, outPut, position):
    bgFrame = cv2.imread(videoFramSrc)
    logo = cv2.imread(imageSrc)

    logo_width, logo_height = logo.shape[1]/2, logo.shape[0]/2

    new_logo = cv2.resize(logo, (logo_width, logo_height))
    mask = 255 * np.ones(new_logo.shape, new_logo.dtype)

    center_x = (position[0] + position[2]/2)
    center_y = (position[1] + position[3]/2)


    print ("origin-x -- origin-y:  ",center_x, center_y)

    #print ("width - height:  ",center_x ,"--",center_y,)

    #print("width - height:  ",l_width/2," -- ",l_height/2)

    global camer_position_y,camer_position_x

    if camer_position_y == 0:
        camer_position_y = center_y

    elif abs(camer_position_y - center_y)>10:
        camer_position_y = center_y
    else:
        camer_position_y = camer_position_y


    if camer_position_x == 0:
        camer_position_x = center_x

    elif abs(camer_position_x - center_x)>3:

        camer_position_x = center_x

    else:
        camer_position_x = camer_position_x

    center = (camer_position_x, camer_position_y)


    mixed_clone = cv2.seamlessClone(new_logo, bgFrame, mask, center, cv2.MIXED_CLONE)

    cv2.imwrite(outPut, mixed_clone)


def reize_image(image):
    image_width, image_height = image.shape[1]/4, image.shape[0]/4
    resize_image = cv2.resize(image, (image_width, image_height))
    return resize_image

def save_position_x(x_positon):
    position_array.append(x_positon)

def resortItem():
    for i in range(0,len(camer_position_x)):
        if i !=0:
            print(camer_position_x[i])
            print(camer_position_y[i])


if __name__ == '__main__':
    #start = time.clock()
    set_tracker_position()
    #resortItem()
    #print(position_array)
    #save_images_from_video("/Users/Allan/Desktop/test.mp4")

    #put_image_to_video("/Users/Allan/Desktop/sky.jpg","/Users/Allan/Desktop/tao.jpg","/Users/Allan/Desktop/xAd/videoImages/1.jpg")
    #print "%s  %s"%("set_tracker_postion", time.clock() - start), "second"