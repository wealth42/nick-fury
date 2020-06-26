#author :-Harsh Vardhan
#script to initialize the database and create a table that will be accessed by the main program
import mysql.connector as mysql
database = mysql.connect(user='root', password='password',host='localhost')
cursor = database.cursor()
cursor.execute("create database database_name;")
cursor.execute("use database_name;")
createDB = "create table data(  id varchar(255),  commonName varchar(255), lat float, lon float, time TIME, NbBikes int,NbDocks int,Locked varchar(20),primary key(id,time));"
cursor.execute(createDB)
database.commit()
cursor.close()
database.close()
