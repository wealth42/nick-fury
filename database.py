import mysql.connector

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root123",
#database="bikestation"
)

print(mydb)

mycursor=mydb.cursor()

#create database 
mycursor.execute("CREATE DATABASE bikestation")





#insert or update
'''
updated_list=mycurson.execute("SELECT * FROM stations")

if(station_name in updated_list):
	sql="UPDATE stations set time=''  where station='station_name' "
else:
	sql="INSERT INTO stations (station,time) VALUES ('%s','%s')"
	value=('station_name','time')

	'''

