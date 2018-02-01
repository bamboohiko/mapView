import matplotlib.pyplot as plt
import geojson
import descartes

import cv2

with open('data.json','r') as f:
	jsonData = f.read()

data = geojson.loads(jsonData)

for feature in data.features:
	if feature.geometry.type == 'LineString':
		x = [i for i,j in feature.geometry.coordinates]
		y = [j for i,j in feature.geometry.coordinates]
	elif feature.geometry.type == 'MultiPolygon':
		for polygon in feature.geometry.coordinates[0]:
			x = [i for i,j in polygon]
			y = [j for i,j in polygon]
	lines = plt.plot(x,y,'k',linewidth=0.1 )


#plt.axis([0, 6, 0, 20])
plt.savefig('test.png',dpi = 1024)
#plt.show()

