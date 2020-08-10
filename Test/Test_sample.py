

# Python program to transform an image using 
# threshold. 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

# Image operation using thresholding 

img = cv2.imread('character'+str(1)+'.jpg') 
print (img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU) 
cv2.imwrite("output/output"+str(1)+".jpg",thresh)


