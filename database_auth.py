from mysql.connector import connect 
from mysql.connector import Error

## change database, user and password as per your configuration.

def connection():
	try:
		connection = connect(
							host = 'localhost',
							database = '',  ## enter database
							user = '',  ## enter user name
							password = '',  ##  enter password for user
							auth_plugin='mysql_native_password'
						)
		return connection
	

	except Error as error:
		return error
