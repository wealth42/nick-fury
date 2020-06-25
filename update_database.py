import database_auth
import requests
import json
from datetime import date
from datetime import datetime
from mysql.connector import Error

connection = database_auth.connection()

api_url = 'https://api.tfl.gov.uk/bikepoint'

try:
	if connection.is_connected():
		cursor = connection.cursor()

		## initilize table with current values
		try:
			r = requests.get(api_url)
			data = json.loads(r.text)

			for i in range(len(data)):
				bikestation_id = data[i]['id'].lower()
				bike = data[i]['additionalProperties'][6]['value']
				empty_docks = data[i]['additionalProperties'][7]['value']
				total_docks = data[i]['additionalProperties'][8]['value']
				current_date = str(date.today())
				current_time = str(datetime.now().strftime('%H:%M:%S'))
				

				try:
					query = "update bikeapitest set bike=%s, empty_docks=%s, total_docks=%s, update_time=%s, update_date=%s where id=%s;"
					val = (bike,empty_docks,total_docks,current_time,current_date,bikestation_id)
					cursor.execute(query,val)
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