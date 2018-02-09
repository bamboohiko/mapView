import matplotlib.pyplot as plt
import numpy as np
import geojson
import cv2
import os

class AreaDivide:

	@classmethod
	def vector2pixel(cls,filename,imgName):
		with open(filename,'r') as f:
			data = geojson.load(f)
		for feature in data.features:
			if feature.geometry.type == 'LineString':
				x = [i for i,j in feature.geometry.coordinates]
				y = [j for i,j in feature.geometry.coordinates]
			elif feature.geometry.type == 'MultiPolygon':
				for polygon in feature.geometry.coordinates[0]:
					x = [i for i,j in polygon]
					y = [j for i,j in polygon]
			lines = plt.plot(x,y,'k',linewidth=0.1 )

		#xmin,xmax = plt.xlim()
		#ymin,ymax = plt.ylim()
		boundary = [plt.xlim(),plt.ylim()]
	
		plt.xticks([])
		plt.yticks([])

		plt.savefig(imgName,dpi = 1024)

		return boundary

	@classmethod
	def pixel2coord(cls,x,y,r,c,boundary):

		nx = boundary[0][0] + x/c*(boundary[0][1]-boundary[0][0])
		ny = boundary[1][1] - y/r*(boundary[1][1]-boundary[1][0])
		return [nx,ny]

	@classmethod
	def pixel2vector(cls,thresh,boundary):
		image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		
		r,c = image.shape
		
		data = geojson.FeatureCollection([])
		for con in contours[3:]:
			poly = geojson.Polygon([[tuple(cls.pixel2coord(p[0][0],p[0][1],r,c,boundary)) for p in con]])
			data.features.append(geojson.Feature(geometry = poly))
		#print(len(contours)-2)

		return data


	@classmethod
	def imageDivide(cls,imgName):
		#read the image and find the outer contours
		img = cv2.imread(imgName,0)
		ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
		image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		
		xmin,ymin = contours[0][0][0]
		xmax,ymax = contours[0][2][0]
		add = 10
		img = img[ymin+add:ymax-add,xmin+add:xmax-add]		
		#the dilation and thin for image
		ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
		kernel = np.ones((4,4),np.uint8)
		erosion = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations = 3)
		erosion = cv2.bitwise_not(erosion)
		#connected components found
		ret, markers = cv2.connectedComponents(erosion)
		img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
		markers = cv2.watershed(img,markers)

		out = cv2.convertScaleAbs(markers + 1)
		ret, thresh = cv2.threshold(out,1,255,cv2.THRESH_BINARY_INV)
		#thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations = 1)
		#cv2.imwrite('thresh.png',thresh)

		return thresh
		
	@classmethod
	def areadivide(cls,filename):

		boundary = cls.vector2pixel(filename,'sav.png')
		thresh = cls.imageDivide('sav.png')
		newdata = cls.pixel2vector(thresh,boundary)

		return newdata

'''
data = AreaDivide.areadivide('data.json')

with open('newdata.js','w') as f:
	f.write('var data = ' + geojson.dumps(data))
'''

