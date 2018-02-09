from rdp import rdp
import os
import geojson

with open('newdata.json','r') as f:
	data = geojson.load(f)

e = 6e-5

for fea in data.features:
	poly = fea.geometry.coordinates[0]
	npoly = rdp(poly,epsilon = e)
	fea.geometry.coordinates[0] = npoly


with open('newnewdata.js','w') as f:
	f.write('var data = ' + geojson.dumps(data))