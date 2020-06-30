import mysql.connector

# Creating the Database in the name of Wealth_BIKE
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Wealth_BIKE")
print("Data base has been created")

mycursor.close()




# Creating the table in the name of london

mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="Wealth_BIKE"
)

mycursor1 = mydb1.cursor()

sql ='''CREATE TABLE london(
   date_time TIMESTAMP(6),
   bike_count INT,place VARCHAR(255)
)'''
print("Table has been created")

mycursor1.execute(sql)

mycursor1.close()






