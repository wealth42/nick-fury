from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
import os

user = os.environ.get('USER')
password = os.environ.get('password')

DB_NAME = 'BikePoints'

TABLES = {}
TABLES['bikes_availablility'] = (
    "CREATE TABLE `bikes_availability` ("
    "  `bikeid` int(11) NOT NULL,"
    "  `nam` varchar(50) NOT NULL,"
    "  `lat` varchar(50) NOT NULL,"
    "  `longitude` varchar(50) NOT NULL,"
    "  `installed` enum('true','false') NOT NULL,"
    "  `locked` enum('true','false') NOT NULL,"
    "   `nbBikes` int(3),"
    "   `nbEmptyDocks`  int(3),"
    "  PRIMARY KEY (`bikeid`)"
    ")")

TABLES['timestamp_bikes_data'] = (
    "CREATE TABLE `timestamp_bikes_data` ("
    "  `bikeid` int(11) NOT NULL,"
    "  `nam` varchar(50) NOT NULL,"
    "  `lat` DECIMAL(10,8) NOT NULL,"
    "  `longitude` DECIMAL(11,8) NOT NULL,"
    "  `installed` enum('true','false') NOT NULL,"
    "  `locked` enum('true','false') NOT NULL,"
    "   `TimeSnap` datetime,"
    "   `nbBikes` int(3),"
    "   `nbEmptyDocks`  int(3),"
    "    CONSTRAINT Bikeid_Time UNIQUE (bikeid, TimeSnap)  "
    ")")


cnx = mysql.connector.connect(user=user, password=password)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()



