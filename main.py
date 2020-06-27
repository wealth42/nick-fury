# Imports
from flask import Flask, render_template
import requests, json
import pandas as pd
import datetime
import mysql.connector
from sqlalchemy import create_engine
import threading
from data import select_user
from dbsecrets import USERNAME, PASSWORD, PORT, DATABASENAME

app = Flask(__name__)

def main():
	
	# Calls the main() function every 300 seconds 
	threading.Timer(300.0, main).start()

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

	return df,data_from_db

# Routing in Flask to render "index.html" template
@app.route("/")
def index():
	data = main()[0] # Now 'data' variable contains the Pandas DataFrame df
	info = main()[1]
	length = len(data)
	return render_template("index.html", data=data,length=length, info=info)


# Running the Flask Application
if __name__ == '__main__':
	app.run(debug=True)
