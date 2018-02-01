import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
img = cv2.imread('test.png',0)
img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
img = cv2.bitwise_not(img)

kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)
fimg = cv2.bitwise_not(erosion)

cv2.imwrite('finish.png',fimg)
'''

img = cv2.imread('test.png',0)
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((4,4),np.uint8)
erosion = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations = 3)
erosion = cv2.bitwise_not(erosion)

ret, markers = cv2.connectedComponents(erosion)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#img = cv2.applyColorMap(img,cv2.COLORMAP_HSV)
markers = cv2.watershed(img,markers)
out = cv2.convertScaleAbs(markers)
out = cv2.applyColorMap(out,cv2.COLORMAP_PARULA)
out[markers == 1] = [255,255,255]
cv2.imwrite('ccl.png',out)

#cv2.imwrite('ccl.png',markers)

#cv2.imwrite('ccl.png',thresh)
'''
ret, markers = cv2.connectedComponents(img)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(img.markers)
img[markers == -1] = [255,255,255]
cv2.imwrite('ccl.png',img)
'''