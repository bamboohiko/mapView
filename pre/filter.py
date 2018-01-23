import os
import json
import math

def areaRule(poly):

	Threshold = -5

	area = 0
	l = len(poly)
	for i in range(0,l-1):
		area += poly[i][0]*poly[i+1][1] - poly[i+1][0]*poly[i][1]

	area = abs(area*0.5) + 1e-13


	return math.floor(math.log10(area)) >= Threshold

def shapeRule(poly):
	return True



with open('data.json','r') as f:
	jsonData = f.read()

data = json.loads(jsonData)
newData = []
#cnt = dict()

for poly in data:
	if areaRule(poly) and shapeRule(poly):
		newData.append(poly)
	'''
	ar = areaRule(poly)
	newData.append(ar)
	try:
		cla = math.floor(math.log10(ar))
	except Exception as e:
		print(poly,ar)
	else:
		pass
	if not cla in cnt.keys():
		cnt.setdefault(cla,0)
	cnt[cla] += 1
	'''

#print(str(cnt.items()))
with open('usedData.json','w') as f:
	f.write(str(newData))

print(len(newData))
