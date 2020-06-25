import mysql.connector

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database="bikestation"
)

mycursor=mydb.cursor()

#CREATE TABLE

mycursor.execute("CREATE TABLE stations (station VARCHAR(255),time VARCHAR(255))")

#check if table exits

