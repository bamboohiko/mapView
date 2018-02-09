import csv
import psycopg2

with open('thailand.csv','r',newline = '', encoding = 'utf8') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	data = [row for row in spamreader]
'''
with open('data.csv','w',newline = '', encoding = 'utf8') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter = ',', quotechar = '"',quoting = csv.QUOTE_MINIMAL)
	for row in data:
		spamwriter.writerow(row)
'''

connection = psycopg2.connect(database = 'postgis_24_sample', user = 'postgres', password = 'password')
cursor = connection.cursor()


cursor.execute('''
	CREATE TABLE IF NOT EXISTS public.thailand (
	)
	WITH (
	    OIDS = FALSE
	);
	ALTER TABLE public.thailand
	    OWNER to postgres;
	''')

for header in data[0]:
	ind = header.find(':')
	if ind != -1:
		header = header[:ind] + '_' + header[ind+1:]
	if header == 'natural':  
		header = '_' + header
	print(header)
	cursor.execute('ALTER TABLE public.thailand ADD COLUMN IF NOT EXISTS ' + header + ' text;')

cursor.execute('''
	copy public.thailand 
	FROM 'D:\\Files\\projects\\functionalArea\\roadNet\\thailand\\thailand.csv' 
	DELIMITER ',' CSV HEADER ENCODING 'UTF8' QUOTE '\"';
	''')

connection.commit()