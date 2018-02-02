import psycopg2
import geojson


connection = psycopg2.connect(database = 'postgis_24_sample', user = 'postgres', password = 'password')
cursor = connection.cursor()

cursor.execute('select st_SetSRID(geom,4326) from public.tha_adm1 where name_1 = \'Bangkok Metropolis\'')
area = cursor.fetchone()[0]
cursor.execute('select st_asgeojson(\''+ area + '\')::jsonb as geometry')
kancore = geojson.FeatureCollection([geojson.Feature(geometry = cursor.fetchone()[0])]);

cursor.execute('''
	select st_asgeojson(st_transform(way,4326))::jsonb as geometry 
	from public.thailand 
	where admin_level = '' and waterway = '' and 
	highway not like '%_link' and highway <> 'tertiary' 
	and (st_covers(\'''' + area + '''\',st_transform(way,4326))
	or st_crosses(\'''' + area + '''\',st_transform(way,4326)));
	''')
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


