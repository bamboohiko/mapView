import cv2
import numpy as np
from matplotlib import pyplot as plt

import os
import json

import geojson

def pixel2coord(x,y):
	nx = xmin + x/c*(xmax-xmin)
	ny = ymax - y/r*(ymax-ymin)
	return [nx,ny]


img = cv2.imread('test_water.png',0)
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

xmin,ymin = contours[0][0][0]
xmax,ymax = contours[0][2][0]
add = 10
img = img[ymin+add:ymax-add,xmin+add:xmax-add]

ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8)
erosion = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations = 3)
erosion = cv2.bitwise_not(erosion)

ret, markers = cv2.connectedComponents(erosion)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
markers = cv2.watershed(img,markers)

out = cv2.convertScaleAbs(markers + 1)
ret, thresh = cv2.threshold(out,1,255,cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



with open('scope.txt','r') as f:
	sc = f.read()

xmin,xmax,ymin,ymax = json.loads(sc)
r,c = out.shape

data = geojson.FeatureCollection([])
for con in contours[2:]:
	poly = geojson.Polygon([[tuple(pixel2coord(p[0][0],p[0][1])) for p in con]])
	data.features.append(geojson.Feature(geometry = poly))

with open('newdata.js','w') as f:
	f.write('var data = ' + geojson.dumps(data))