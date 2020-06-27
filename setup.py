# Setting up the Local Database with MySQL
import mysql.connector
from dbsecrets import USERNAME, PASSWORD, PORT

db = mysql.connector.connect(user=USERNAME, #Your Database Username
							  password = PASSWORD, # Your Database Password
							  host = "localhost",
							  )

# Making a cursor object for Database
my_cursor = db.cursor()

# Creating the Database
my_cursor.execute("CREATE DATABASE local_database")

""" Creating Table "info" with following Columns
	*id - Primary Key
	*commonName - Name of the Place	
	*lat - Latitude of the Place
	*lon - Longitude of the Place
	*nbBikes - Number of Bikes
	*nbDocks - Number of Docks
	*nbEmpty - Number of Empty Docks
	*time - Current Time
"""
my_cursor.execute("USE local_database")
my_cursor.execute("CREATE TABLE info(id VARCHAR(255), commonName VARCHAR(255),  lat float, lon float, nbBikes VARCHAR(10), nbDocks VARCHAR(10),nbEmpty VARCHAR(10),time VARCHAR(255))")
db.commit()
db.close()

