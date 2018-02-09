import psycopg2
import geojson


connection = psycopg2.connect(database = 'postgis_24_sample', user = 'postgres', password = 'password')
cursor = connection.cursor()

#area
areaName = '\'Bangkok Metropolis\''

cursor.execute('select st_SetSRID(geom,4326) from public.tha_adm1 where name_1 = ' + areaName)
area = cursor.fetchone()[0]

cursor.execute('select st_asgeojson(\''+ area + '\')::jsonb as geometry')

kancore = geojson.FeatureCollection([geojson.Feature(geometry = cursor.fetchone()[0])]);

#waterway,highway and railway
highway = ['\'motorway\'','\'trunk\'','\'primary\'','\'secondary\'','\'tertiary\'']
waterway = ['\'canal\'','\'river\'','\'stream\'']
railway = ['\'rail\'']

highway_switch = [True,True,True,True,False]
waterway_switch = [False,False,False]
railway_switch = [False]

cond = []
for i in range(0,len(highway)):
	if highway_switch[i]:
		cond.append('highway = ' + highway[i])
for i in range(0,len(waterway)):
	if waterway_switch[i]:
		cond.append('waterway = ' + waterway[i])
for i in range(0,len(railway)):
	if railway_switch[i]:
		cond.append('railway = ' + railway[i])

condStr = ' or '.join(cond)
if len(condStr) > 0:
	condStr = '(' + condStr + ')'

#query
cursor.execute('''
	select st_asgeojson(st_transform(way,4326))::jsonb as geometry 
	from public.thailand where ''' + condStr + '''
	and (st_covers(\'''' + area + '''\',st_transform(way,4326))
	or st_crosses(\'''' + area + '''\',st_transform(way,4326)));
	''')
#	highway not like '%_link' and highway <> 'tertiary' 
#	where highway <> \'\' 
#	and (st_covers(\'''' + area + '''\',st_transform(way,4326))
#	or st_crosses(\'''' + area + '''\',st_transform(way,4326)));

for linestring in cursor:
	fea = geojson.Feature(geometry = linestring[0])
	kancore.features.append(fea)

with open('data.json','w') as f:
	f.write(geojson.dumps(kancore))

with open('data.js','w') as f:
	f.write('var data = ' + geojson.dumps(kancore))