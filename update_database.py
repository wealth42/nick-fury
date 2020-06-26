import requests
import json
from datetime import date
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import database_credentials as dc
from table_skeleton import Base,Table

def connect_with_database():
	path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(dc.USER_NAME,dc.USER_PASS,dc.DATABASE_PORT,dc.DATABASE_NAME)
	engine = sqlalchemy.create_engine(path)
	return engine


def create_session(engine):
	Session = sqlalchemy.orm.sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	return session

def update_table(session):
	api_url = 'https://api.tfl.gov.uk/bikepoint'
	try:
		r = requests.get(api_url)
		data = json.loads(r.text)

		for i in range(len(data)):
			bikestation_id = data[i]['id'].lower()
			bike = data[i]['additionalProperties'][6]['value']
			empty_docks = data[i]['additionalProperties'][7]['value']
			total_docks = data[i]['additionalProperties'][8]['value']
			current_date = str(date.today())
			current_time = str(datetime.now().strftime('%H:%M:%S'))

			result = session.query(Table).filter(Table.bike_id==bikestation_id).one()
			result.bike = bike
			result.empty_docks = empty_docks
			result.total_docks = total_docks
			result.update_date = current_date
			result.update_time = current_time
		session.commit()

	except:
		print("API is not reachable.")
	pass


if __name__=="__main__":
	engine = connect_with_database()
	session = create_session(engine)
	update_table(session)
	pass