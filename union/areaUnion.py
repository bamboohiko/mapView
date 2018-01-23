import os
import json
import math

def distance(pa,pb):
	dx = pa[0] - pb[0]
	dy = pa[1] - pb[1]
	return math.sqrt(dx*dx+dy*dy)

def areaFig(poly):
	area = 0
	l = len(poly)
	for i in range(0,l-1):
		area += poly[i][0]*poly[i+1][1] - poly[i+1][0]*poly[i][1]
		'''
		try:
			area += poly[i][0]*poly[i+1][1] - poly[i+1][0]*poly[i][1]
		except Exception as e:
			print(poly[i],poly[i+1])
		else:
			pass
		'''
			
	area = abs(area*0.5) + 1e-13

	return area

def areaUnionFor2(lista,listb):
	la = len(lista)
	lb = len(listb)
	listDis = []
	for i in range(0,la):
		for j in range(0,lb):
			listDis.append([i,j,distance(lista[i],listb[j])])

	lista += lista[0:-1]
	listb += listb[0:-1]

	listDis.sort(key= lambda x:(x[2],x[0],x[1]))
	x1 = listDis[0][0]
	y1 = listDis[0][1]
	
	x2 = listDis[2][0]
	y2 = listDis[2][1]

	if (y2 > y1):
		poly1 = [lista[x1]] + listb[y1:y2] + lista[x2:x1+la]
		poly2 = lista[x1:x2] + listb[y2:y1+lb] + [lista[x1]]
	else:
		poly1 = lista[x1] + listb[y1:y2+lb] + lista[x2:x1+la]
		poly2 = lista[x1:x2] + listb[y2:y1] + lista[x1]

	if areaFig(poly1) > areaFig(poly2):
		return poly1
	else:
		return poly2

with open('data.json', 'r') as f:
	jsonData = f.read()

data = json.loads(jsonData)

print(areaUnionFor2(data[0],data[1]))
