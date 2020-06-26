import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

### define schema of table
class Table(Base):
	__tablename__='bikeapi'
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	bike_id = sqlalchemy.Column(sqlalchemy.String(length=30))
	common_name = sqlalchemy.Column(sqlalchemy.String(length=70))
	terminal_id = sqlalchemy.Column(sqlalchemy.String(length=10))
	bike = sqlalchemy.Column(sqlalchemy.Integer)
	empty_docks = sqlalchemy.Column(sqlalchemy.Integer)
	total_docks = sqlalchemy.Column(sqlalchemy.Integer)
	update_time = sqlalchemy.Column(sqlalchemy.String(length=20))
	update_date = sqlalchemy.Column(sqlalchemy.String(length=20))