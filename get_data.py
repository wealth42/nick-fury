import requests, json
import pandas as pd
import datetime
import mysql.connector

from sqlalchemy import create_engine
from dbsecrets import USERNAME, PASSWORD, PORT, DATABASENAME
from data import select_user

def main():
	
	# Reading API data into Pandas DataFrame
	df = pd.read_json(r"https://api.tfl.gov.uk/BikePoint")

	# Removing unwanted columns from DataFrame
	df = df.drop(["$type","url","placeType","children","childrenUrls"], axis=1)

	# Extracting NbBikes, NbDocks and NbEmpty from API
	def get_elements(dataframe):
		for element in dataframe:
			if element["key"] == "NbBikes":
				df["nbBikes"] = element["value"]
			elif element["key"] == "NbDocks":
				df["nbDocks"] = element["value"]
			elif element["key"] == "NbEmptyDocks":
				df["nbEmpty"] = element["value"]


	df["additionalProperties"].apply(get_elements)
	df = df.drop(["additionalProperties" ], axis = 1)

	# Adding TimeStamp
	df["time"] = datetime.datetime.now()

	# Creating sqlalchemy Engine
	engine = create_engine('mysql+pymysql://' + '{}:{}@{}/{}'.format(USERNAME,PASSWORD,"localhost",DATABASENAME))

	# Sending data to Local Database
	df.to_sql("info", engine, if_exists="append", index=False)

	# Getting Data from data.py file
	data_from_db = select_user()

	return df

# Setting up the Database
mydb = mysql.connector.connect(
  host="localhost",
  user=USERNAME,
  passwd=PASSWORD,
  database= DATABASENAME
)

# Setting up the cursor for DB
mycursor = mydb.cursor(prepared=True)


def select_user():
	sql = "SELECT * FROM info WHERE time = (SELECT max(time) FROM info ) ORDER BY id, time;"
	mycursor.execute(sql)	
	info = mycursor.fetchall()

	info = [list(ele) for ele in info]
	return info