import os

USERNAME = os.environ.get("db_username", "admin")
PASSWORD = os.environ.get("db_password", "admin")
PORT = int(os.environ.get("db_port", 3306))
DATABASENAME = os.environ.get("db_name","local_database")