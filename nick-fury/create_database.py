import datetime
import MySQLdb
import time
import getpass

password = getpass.getpass()  #ENTER YOUR PASSWORD in cmd

con = MySQLdb.connect(host='localhost',
							user='root',
							passwd=password)
cur = con.cursor()

try:
	cur.execute("CREATE DATABASE bikepoint;")

	db = MySQLdb.connect(host='localhost',
						user='root',
						passwd=password,
						db="bikepoint")

	cursor = db.cursor()
	cursor.execute("CREATE TABLE terminal(Terminal_id VARCHAR(45) NOT NULL, CommonName VARCHAR(200) NOT NULL, TerminalName VARCHAR(45) NOT NULL, PRIMARY KEY (Terminal_id));")
	db.commit()

	cursor.execute("CREATE TABLE terminal_info(TerminalName VARCHAR(45) NOT NULL, nbBike int(11) NOT NULL, nbEmptyDock int(11) NOT NULL, nbDock int(11) NOT NULL, datet datetime NOT NULL, PRIMARY KEY (TerminalName,datet));")
	db.commit()

except Exception as e:
	print("Database bikepoint already exist")
	pass

try:
	cur.execute("CREATE DATABASE realtimebikepoint;")

	db = MySQLdb.connect(host='localhost',
						user='root',
						passwd=password,
						db="realtimebikepoint")

	cursor = db.cursor()
	cursor.execute("CREATE TABLE terminal(Terminal_id VARCHAR(45) NOT NULL, CommonName VARCHAR(200) NOT NULL, TerminalName VARCHAR(45) NOT NULL, PRIMARY KEY (Terminal_id));")
	db.commit()

	cursor.execute("CREATE TABLE terminal_info(TerminalName VARCHAR(45) NOT NULL, nbBike INT(11) NOT NULL, nbEmptyDock INT(11) NOT NULL, nbDock INT(11) NOT NULL, datet datetime NOT NULL, PRIMARY KEY (TerminalName,datet));")
	db.commit()
except:
	print("Database realtimebikepoint already exist")
	pass
