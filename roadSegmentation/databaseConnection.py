import csv
import psycopg2

#connection establishment
class DatabaseConnection():

	__connection = 0
	__cursor = 0

	__database = ''
	__user = ''
	__password = ''

	
	def __init__(self,database,user,password):
		self.__database,self.__user,self.__password = [database,user,password]
		
		self.__connection = psycopg2.connect(database = database, user = user, password = password)
		self.__cursor =  self.__connection.cursor()
		
	def dataImport(self, csvfileName, tablename):
		with open(csvfileName,'r',newline = '', encoding = 'utf8') as csvfile:
			spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
			data = [row for row in spamreader]

		

		self.__tableBuild(tablename)
		self.__headerBuild(tablename,data[0])

		self.__cursor.execute('''
		copy public.thailand 
		FROM '{}'
		DELIMITER ',' CSV HEADER ENCODING 'UTF8' QUOTE '\"';
		'''.format(csvfileName))

		self.__connection.commit()

	def __tableBuild(self,tablename):
		self.__cursor.execute('''
		CREATE TABLE IF NOT EXISTS {} (

		)
		WITH (
		    OIDS = FALSE
		);
		ALTER TABLE {}
		    OWNER to {};
		'''.format(tablename,tablename,self.__user))

		self.__connection.commit()

	def __headerBuild(self,tablename,headers):
		for header in headers:
			#replace the colon
			ind = header.find(':')
			if ind != -1:
				header = header[:ind] + '_' + header[ind+1:]
			#keyword should be add an underline
			if header == 'natural':
				header = '_' + header
			self.__cursor.execute('ALTER TABLE {} ADD COLUMN IF NOT EXISTS {} text;'.format(tablename,header))

		self.__connection.commit()	

	def getCursor(self):
		return self.__cursor

'''
connection = DatabaseConnection(database = 'postgis_24_sample', user = 'postgres', password = 'password')

filename = 'D:\\Files\\projects\\functionalArea\\roadNet\\thailand\\thailand.csv'
connection.dataImport(filename,tablename = 'public.thailand')
'''