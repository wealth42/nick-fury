import mysql.connector
from dbsecrets import USERNAME, PASSWORD, PORT, DATABASENAME

# Setting up the Database
mydb = mysql.connector.connect(
  host="localhost",
  user=USERNAME,
  passwd=PASSWORD,
  database= DATABASENAME
)

# Setting up the cursor for DB
mycursor = mydb.cursor(prepared=True)


def select_user():
	sql = "SELECT * FROM info WHERE time = (SELECT max(time) FROM local_database.info ) ORDER BY id, time;"
	mycursor.execute(sql)	
	info = mycursor.fetchall()

	info = [list(ele) for ele in info]
	length = len(info)
	return info, length