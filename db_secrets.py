import os

USERNAME = os.environ.get("db_username", "root")
PASSWORD = os.environ.get("db_password", "")
PORT = int(os.environ.get("db_port", 3306))
DATABASENAME = os.environ.get("db_name")