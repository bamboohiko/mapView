import cv2
import numpy as np

img = cv2.imread('test.png',0)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('finish.png',dilation)