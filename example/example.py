from roadSegmentation.databaseConnection import DatabaseConnection
from roadSegmentation.dataCleaning import DataCleaning
from roadSegmentation.areaDivide import AreaDivide
import geojson

#建立database连接
connection = DatabaseConnection(database = 'postgis_24_sample', user = 'postgres', password = 'password')

'''
#导入csv文件
filename = 'D:\\Files\\projects\\functionalArea\\roadNet\\thailand\\thailand.csv'
connection.dataImport(filename,tablename = 'public.thailand')
'''

#查询
collector = DataCleaning.query(connection = connection,areaTable = 'public.tha_adm1',areaName = '\'Bangkok Metropolis\'',roadTable = 'public.thailand',roadOpinions = [])

with open('data.json','w') as f:
	f.write(geojson.dumps(collector))

#区域划分
data = AreaDivide.areadivide('data.json')

with open('divideData.js','w') as f:
	f.write('var data = ' + geojson.dumps(data))

