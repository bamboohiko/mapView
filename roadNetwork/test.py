import os
import json

with open('scope.txt','r') as f:
	sc = f.read()

print(json.loads(sc))
xmin,xmax,ymin,ymax = json.loads(sc)