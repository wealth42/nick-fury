import database_auth
import requests
import json
from datetime import date
from datetime import datetime
from mysql.connector import Error

connection = database_auth.connection()


try:
	if connection.is_connected():
		cursor = connection.cursor()
		fetch_query = 'select common_name from bikeapitest;'
		cursor.execute(fetch_query)
		records = cursor.fetchall()
		records = [str(record[0]).lower() for record in records]

		###get input from user
		place = input("Enter place name : ")
		place = place.lower()

		## find match_cases from records
		match_cases = [record for record in records if place in record]
		print("Total Match Cases are: ",len(match_cases))

		###fetch values from database
		for i in range(len(match_cases)):
			query = 'select * from bikeapitest where common_name="'+match_cases[i]+'";'
			cursor.execute(query)
			results = cursor.fetchall()
			print("------------ RESULT - "+str(i+1)+"-------------")
			print("Commaon Name : "+results[0][1])
			print("Terminal ID : "+str(results[0][2]))
			print("Number of Available Bikes : "+str(results[0][3]))
			print("Number of Empty Docks : "+str(results[0][4]))
			print("Number of Total Docks : "+str(results[0][5]))
			print("Last Update Time : "+str(results[0][6]))
			print("Last Update Date : "+str(results[0][7]))
			print("\n")

		cursor.close()
		connection.close()

except Error as error:
	print(error)