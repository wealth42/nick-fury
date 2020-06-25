import database_auth
import requests
import json
from mysql.connector import Error

connection = database_auth.connection()

api_url = 'https://api.tfl.gov.uk/bikepoint'


try:
	if connection.is_connected():
		cursor = connection.cursor()
		## create table in database
		create_table_query = "create table bikeapitest(id varchar(30) NOT NULL, common_name varchar(70) NOT NULL, terminal_id int NOT NULL, bike int, empty_docks int, total_docks int,update_time varchar(20), update_date varchar(20), CONSTRAINT UC_bikeapi UNIQUE(id, terminal_id));"
		cursor.execute(create_table_query)
		connection.commit()

		## initilize table with current values
		try:
			r = requests.get(api_url)
			data = json.loads(r.text)

			for i in range(len(data)):
				bikestation_id = data[i]['id'].lower()
				common_name = data[i]['commonName'].lower()
				terminal_id = data[i]['additionalProperties'][0]['value']

				try:
					insert_query = 'insert into bikeapitest(id, common_name,terminal_id) values(%s,%s,%s);'
					val = (bikestation_id,common_name,terminal_id)
					cursor.execute(insert_query,val)
				except Error as error:
					print(error)
					cursor.close()
					connection.close()
			connection.commit()
			cursor.close()
			connection.close()

		except:
			print("API key is not reachable.")
			cursor.close()
			connection.close()

except:
	print("error while connecting database. generated error as follow: "+str(connection))