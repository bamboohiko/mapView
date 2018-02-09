import os
import geojson
import math
import copy

EPS = 1e-13

def distance(pa,pb):
	dx = pa[0] - pb[0]
	dy = pa[1] - pb[1]
	return math.sqrt(dx*dx+dy*dy)

def areaRule(poly):

	Threshold = -9

	area = 0
	l = len(poly)
	for i in range(0,l-1):
		area += poly[i][0]*poly[i+1][1] - poly[i+1][0]*poly[i][1]

	area = abs(area*0.5) + EPS


	return math.log10(area) + EPS >= Threshold

def shapeRule(poly):
	Threshold = -3.25

	area = 0
	l = len(poly)
	for i in range(0,l-1):
		area += poly[i][0]*poly[i+1][1] - poly[i+1][0]*poly[i][1]

	area = abs(area*0.5) + EPS

	diag = 0

	for pa in poly:
		for pb in poly:
			diag = max(diag,distance(pa,pb))

	return math.log10(area/diag) + EPS >= Threshold



with open('th2.json','r') as f:
	jsonData = f.read()

data = geojson.loads(jsonData)
newData = copy.deepcopy(data) 
newData.features = []

cnt = 0

for polygon in data.features:
	if polygon.geometry is None:
		continue
	locs = polygon.geometry.coordinates[0]
	if areaRule(locs) and shapeRule(locs):
		newData.features.append(polygon)
	'''
	ar = areaRule(poly)
	sr = shapeRule(poly)

	try:
		cla = math.floor(math.log10(sr))
	except Exception as e:
		print(poly,ar)
	else:
		pass
	if not cla in cnt.keys():
		cnt.setdefault(cla,0)
	cnt[cla] += 1
	'''

#print(str(cnt.items()))
with open('data.js','w') as f:
	f.write('var data = ' + geojson.dumps(newData))