import mysql.connector
#to add time 
import datetime

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database="bikestation"
)

mycursor=mydb.cursor()

sql="INSERT INTO stations (station,time) values(%s,%s)"


x=datetime.datetime.now()
time=x.strftime("%I:%M %p")
value=("gorewell street",time)

mycursor.execute(sql,value)
mydb.commit()

