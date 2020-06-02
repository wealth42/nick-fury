import mysql.connector as mysql
db = mysql.connect(user='root', password='',host='localhost')
cursor = db.cursor()
cursor.execute("create database db;")
cursor.execute("use db;")
createDB = "create table data(  id varchar(255),  commonName varchar(255), lat float, lon float, time TIME, NbBikes int,NbDocks int,primary key(id,time));"
cursor.execute(createDB)
db.commit()
cursor.close()
db.close()
