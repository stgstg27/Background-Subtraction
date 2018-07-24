########################Background Subtraction##########################################
#####Thesis : Application of Machine Learning in Biomdeical diagnosis and therapies#####
################### Author : Saurabh Khandelwal	########################################
###################Shafiee Lab,Harvard Medical School ##################################


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbgAdaptiveGaussain = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbgBayesianSegmentation = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
  ret, frame = cap.read()
  fgmask = fgbg.apply(frame)
  fgbgAdaptiveGaussainmask = fgbgAdaptiveGaussain.apply(frame)
  fgbgBayesianSegmentationmask = fgbgBayesianSegmentation.apply(frame)
  fgbgBayesianSegmentationmask = cv2.morphologyEx(fgbgBayesianSegmentationmask,cv2.MORPH_OPEN,kernel)
  
  cv2.namedWindow('Background Subtraction Bayesian Segmentation',0)
  cv2.namedWindow('Background Subtraction',0)
  cv2.namedWindow('Background Subtraction Adaptive Gaussian',0)
  cv2.namedWindow('Original',0)

  cv2.resizeWindow('Original', 300,300)
  cv2.imshow('Background Subtraction Bayesian Segmentation',fgbgBayesianSegmentationmask)
  cv2.imshow('Background Subtraction',fgmask)
  cv2.imshow('Background Subtraction Adaptive Gaussian',fgbgAdaptiveGaussainmask)
  cv2.imshow('Original',frame)
  
  k = cv2.waitKey(1) & 0xff
  
  if k==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
print ('Program Closed')


