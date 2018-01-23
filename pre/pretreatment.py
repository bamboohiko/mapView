import os
import json


with open('th2.json','r') as f:
	jsonData = f.read()

data = json.loads(jsonData)
sav = []

for area in data['features']:
	if not area['geometry'] is None:
		locs = area['geometry']['coordinates'][0]
		sav.append(locs)

with open('data.json','w') as f:
	f.write(str(sav))