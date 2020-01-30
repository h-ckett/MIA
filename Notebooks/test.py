# imports start
import cv2
import numpy as np
from skimage.filters import threshold_multiotsu
# imports end

# frameCapture start
# Function to extract frames
def frameCapture(fc_path):
    fc_vidObj = cv2.VideoCapture(fc_path) # Path to video file
    fc_count = 0                          # Used as counter variable
    fc_success = 1                        # Checks if the frames were extracted
    
    while fc_success:
        # vidObj object calls read
        fc_success, fc_image = fc_vidObj.read()
        fc_image = cv2.cvtColor(fc_image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
        fc_image = cv2.GaussianBlur(fc_image,(5,5),0) # Gaussian noise filtering
        (threshold, fc_image) = cv2.threshold(fc_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # Normalize & Segment
        cv2.imwrite("frame%d.jpg" % fc_count, fc_image) # Saves the frames
        fc_count += 1
# frameCapture end
        
# frameCaptureMulti start
# Function to extract frames [multi-otsu thresholding]
def frameCaptureMulti(fc_path):
    fc_vidObj = cv2.VideoCapture(fc_path) # Path to video file
    fc_count = 0                          # Used as counter variable
    fc_success = 1                        # Checks if the frames were extracted
    
    while fc_success:
        # vidObj object calls read
        fc_success, fc_image = fc_vidObj.read()
        fc_image = cv2.cvtColor(fc_image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
        fc_image = cv2.GaussianBlur(fc_image,(5,5),0) # Gaussian noise filtering
        fc_thresholds = threshold_multiotsu(fc_image)
        fc_regions = np.digitize(fc_image, bins=fc_thresholds)
        cv2.imwrite("frame%d.jpg" % fc_count, fc_regions) # Saves the frames
        fc_count += 1
# frameCaptureMulti end

# driver code start
# Testing on a mouse video
frameCapture("PATH") # Make sure to edit "PATH" to path to a video here
# driver code end

# Note: frameCapture() functions fine, but frameCaptureMulti() just outputs black frames...
# The issue is not with the grayscale conversion or the gaussian filtering (both tested)
# There is a Stack Overflow question opened here: https://stackoverflow.com/questions/59990709/scikit-image-threshold-multiotsu-outputting-black-frames-from-video
