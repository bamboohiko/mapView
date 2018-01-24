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

def areaUnionFor2(polya,polyb):

	EPS = 1e-13

	polya = polya[:-1]
	polyb = polyb[:-1]

	la = len(polya)
	lb = len(polyb)

	psta = 0
	maxDis = distance(polya[0],polyb[0])
	for i in range(0,la):
		for j in range(0,lb):
			disab = distance(polya[i],polyb[j])
			if (disab > maxDis):
				maxDis = disab
				psta = i
	polya = polya[psta:] + polya[:psta]

	listDis = []
	for i in range(0,la):
		for j in range(0,lb):
			listDis.append([i,j,distance(polya[i],polyb[j])])
	listDis.sort(key= lambda x:(x[2],x[0],x[1]))

	lista = polya
	listb = 2*polyb

	stand = listDis[0][2] + EPS
	phi = 2.0

	kend = len(listDis)
	
	for k in range(0,len(listDis)):
		if listDis[k][2] >= phi*stand:
			kend = k
			break
	print(kend)	
	listDis = [pp[0:2] for pp in listDis]

	p = [listDis[0],listDis[1]]
	mp = (listDis[1][0]-listDis[0][0]) + (listDis[0][1]-listDis[1][1]+lb)%lb
	for i in range(0,kend):
		for j in range(i+1,kend):
			c1,c2 = listDis[i],listDis[j]
			if c1[0] > c2[0]:
				c1,c2 = [c2,c1]
			#print(c1,c2)
			if (c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb > mp:
				mp = (c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb
				p = [c1,c2]
	
	x1,y1 = p[0]
	x2,y2 = p[1]
	if (y2 > y1):
		poly = lista[:x1+1] + listb[y1:y2+1] + lista[x2:] + [lista[0]]
	else:
		poly = lista[:x1+1] + listb[y1:y2+lb+1] + lista[x2:] + [lista[0]]
	return poly

with open('data.json', 'r') as f:
	jsonData = f.read()

data = json.loads(jsonData)

unionPoly = data[0]

for i in range(1,len(data)):
	unionPoly = areaUnionFor2(data[i],unionPoly)
	print(len(unionPoly))

#print((areaUnionFor2(data[2],data[0]))) 
print(unionPoly)
