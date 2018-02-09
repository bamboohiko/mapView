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

cond = ['(highway = \'motorway\' or highway = \'trunk\' or highway = \'primary\' or highway = \'secondary\')',
		'(highway = \'tertiary\')',
		'(waterway = \'stream\')',
		'(waterway = \'canal\')',
		'(waterway = \'river\')',
		'(railway = \'rail\')']

cnt = 0
with open('data.js','w') as f:
		f.write('var data = new Array();\n')
with open('data.js','a') as f:
		f.write('data[0] = ' + geojson.dumps(kancore) + ';\n')

for c in cond:
	cursor.execute('''
		select st_asgeojson(st_transform(way,4326))::jsonb as geometry 
		from public.thailand where ''' + c + '''
		and (st_covers(\'''' + area + '''\',st_transform(way,4326))
		or st_crosses(\'''' + area + '''\',st_transform(way,4326)));
		''')
	
	collector = geojson.FeatureCollection([])
	for linestring in cursor:
		fea = geojson.Feature(geometry = linestring[0])
		collector.features.append(fea)

	cnt += 1
	with open('data.js','a') as f:
		f.write('data[' + str(cnt) + '] = ' + geojson.dumps(collector) + ';\n')
	