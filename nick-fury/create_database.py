import datetime
import MySQLdb
import time
import getpass
import secret

con = MySQLdb.connect(host=secret.host,
							user=secret.user,
							passwd=secret.password)
cur = con.cursor()

try:
	cur.execute("CREATE DATABASE "+secret.db1+";")

	db = MySQLdb.connect(host=secret.host,
						user=secret.user,
						passwd=secret.password,
						db=secret.db1)

	cursor = db.cursor()
	cursor.execute("CREATE TABLE terminal(Terminal_id VARCHAR(45) NOT NULL, CommonName VARCHAR(200) NOT NULL, TerminalName VARCHAR(45) NOT NULL, PRIMARY KEY (Terminal_id));")
	db.commit()

	cursor.execute("CREATE TABLE terminal_info(TerminalName VARCHAR(45) NOT NULL, nbBike int(11) NOT NULL, nbEmptyDock int(11) NOT NULL, nbDock int(11) NOT NULL, datet datetime NOT NULL, PRIMARY KEY (TerminalName));")
	db.commit()

except Exception as e:
	print("Database "+ secret.db1 +" already exist")
	pass

try:
	db2=secret.db2
	cur.execute("CREATE DATABASE "+secret.db2+";")

	db = MySQLdb.connect(host=secret.host,
						user=secret.user,
						passwd=secret.password,
						db=secret.db2)

	cursor = db.cursor()
	cursor.execute("CREATE TABLE terminal(Terminal_id VARCHAR(45) NOT NULL, CommonName VARCHAR(200) NOT NULL, TerminalName VARCHAR(45) NOT NULL, PRIMARY KEY (Terminal_id));")
	db.commit()

	cursor.execute("CREATE TABLE terminal_info(TerminalName VARCHAR(45) NOT NULL, nbBike INT(11) NOT NULL, nbEmptyDock INT(11) NOT NULL, nbDock INT(11) NOT NULL, datet datetime NOT NULL, PRIMARY KEY (TerminalName,datet));")
	db.commit()
except Exception as e:
	print("Database "+ secret.db2 +" already exist")
	pass
