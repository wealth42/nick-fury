import mysql.connector as mysql
db = mysql.connect(user='root', password='',host='localhost')
cursor = db.cursor()
cursor.execute("create database db1;")
cursor.execute("use db1;")
createDB = "create table data(  id varchar(255),  commonName varchar(255), lat float, lon float, time TIME, NbBikes varchar(20),primary key(id,time));"
cursor.execute(createDB)
db.commit()
cursor.close()
db.close()
