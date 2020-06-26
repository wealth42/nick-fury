import mysql.connector
from mysql_details import *


def create_db():
    try:
        # create connection object
        conn=mysql.connector.connect(host=Host,user=Username,passwd=Password)

        #creating cursor object
        mycursor=conn.cursor()

        #create Database
        mycursor.execute("CREATE DATABASE bikepoints")

        #use database bikepoints
        mycursor.execute("USE bikepoints")

        #create table "bikepoints data"  for storing real time bike availability data across London
        mycursor.execute("""CREATE TABLE `bikepoints data` (
        `ID` INT NOT NULL PRIMARY KEY,
        `Name` VARCHAR(100) NOT NULL,
        `Locked` VARCHAR(45) NULL,
        `Total Docks` INT NULL,
        `Available Bikes` INT NULL,
        `Empty Docks` INT NULL,
        `Latitude` DOUBLE NULL,
        `Logitude` DOUBLE NULL,
        `Last Update` DATETIME NULL);""")


        print("Table 'bikepoints data' created successfully.")

    except Exception as e:
        print(e)

    finally:
        conn.close()


if __name__=="__main__":
    create_db()
