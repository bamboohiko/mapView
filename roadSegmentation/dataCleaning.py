import psycopg2
import geojson
#import databaseConnection

class DataCleaning:
	__cursor = 0

	#condition of query
	#use boundary of GDAM database
	@classmethod
	def __areaCondition(cls,areaName,tableName):
		cls.__cursor.execute('select st_SetSRID(geom,4326) from {} where name_1 = {};'.format(tableName,areaName))
		area = cls.__cursor.fetchone()[0]

		return(area)

	@classmethod
	def __roadCondition(cls,roadOpinions,tableName):
		#waterway,highway and railway
		highway = ['\'motorway\'','\'trunk\'','\'primary\'','\'secondary\'','\'tertiary\'']
		waterway = ['\'canal\'','\'river\'','\'stream\'']
		railway = ['\'rail\'']

		highway_switch = [True,True,True,True,False]
		waterway_switch = [False,True,False]
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

		return condStr

	@classmethod
	def query(cls,connection,areaTable,areaName,roadTable,roadOpinions = []):
		cls.__cursor = connection.getCursor()

		collector = geojson.FeatureCollection([]);

		areaStr = cls.__areaCondition(areaName,areaTable)
		roadStr = cls.__roadCondition(roadOpinions,roadTable)

		#add the boundary of area to collector
		cls.__cursor.execute('select st_asgeojson(\'{}\')::jsonb as geometry'.format(areaStr))
		collector.features.append(geojson.Feature(geometry = cls.__cursor.fetchone()[0]))
		
		#add the roads in boundary to collector
		cls.__cursor.execute('''
		select st_asgeojson(st_transform(way,4326))::jsonb as geometry 
		from {} where {}
		and (st_covers(\'{}\',st_transform(way,4326))
		or st_crosses(\'{}\',st_transform(way,4326)));
		'''.format(roadTable,roadStr,areaStr,areaStr))
		for LineString in cls.__cursor:
			fea = geojson.Feature(geometry = LineString[0])
			collector.features.append(fea)

		return collector

'''
connection = databaseConnection.DatabaseConnection(database = 'postgis_24_sample', user = 'postgres', password = 'password')

collector = DataCleaning.query(connection,'\'Bangkok Metropolis\'','public.tha_adm1',[True],'public.thailand')
with open('data.json','w') as f:
	f.write(geojson.dumps(collector))
'''

#json for showing road network
#with open('data.js','w') as f:
#	f.write('var data = ' + geojson.dumps(collector))

