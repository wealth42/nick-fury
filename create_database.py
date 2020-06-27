from sqlalchemy import create_engine
from mysql_details import *


def create_db():
    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}".format(Username, Password, Host))

        # create connection object
        conn=engine.connect()

        #create Database
        conn.execute("CREATE DATABASE bikepoints")

        #use database bikepoints
        conn.execute("USE bikepoints")

        #create table "bikepoints data"  for storing real time bike availability data across London
        conn.execute("""CREATE TABLE `bikepoints data` (
        `ID` INT NOT NULL PRIMARY KEY,
        `Name` VARCHAR(100) NOT NULL,
        `Locked` VARCHAR(45) NULL,
        `TotalDocks` INT NULL,
        `AvailableBikes` INT NULL,
        `EmptyDocks` INT NULL,
        `Latitude` DOUBLE NULL,
        `Logitude` DOUBLE NULL,
        `LastUpdate` DATETIME NULL);""")


        print("Table 'bikepoints data' created successfully.")

    except Exception as e:
        print(e)

    finally:
        conn.close()


if __name__=="__main__":
    create_db()
