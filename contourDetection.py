# THIS IS TO START TO WORK ON DETECTING WHAT THE GARMENTS ARE TO ADD TO THE GARMENT LAYER

import csv
import cv2
import colorDetection
#import image
import sys
import numpy as np
import io
import webcolors

#imgStore = ('data/' + topIDread+'.jpeg')

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",0,300,empty)
cv2.createTrackbar("Threshold2","Parameters",20,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

img = cv2.imread('data/946.jpeg')

imgBlur = cv2.GaussianBlur(img, (7,7), 1)
imgGrey = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

#CODE FROM: https://github.com/murtazahassan/OpenCV-Python-Tutorials-for-Beginners/blob/master/Intermediate/RealTime_Shape_Detection_Contours.py
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
imgCanny = cv2.Canny(imgGrey, threshold1, threshold2)
imgStack = stackImages(0.2,([img, imgCanny, imgGrey]))
cv2.imshow('image', imgCanny)
cv2.waitKey(10000)