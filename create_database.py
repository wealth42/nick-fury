import requests
import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import database_credentials as dc
from table_skeleton import Base,Table


### connect with mysql database using user credentials
def connect_with_database():
	path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(dc.USER_NAME,dc.USER_PASS,dc.DATABASE_PORT,dc.DATABASE_NAME)
	engine = sqlalchemy.create_engine(path)
	return engine



### create table function
def create_table(engine):
	
	Base.metadata.create_all(engine)
	pass

### create session execute query and commit changes to database
def create_session(engine):
	Session = sqlalchemy.orm.sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	return session


### first time initilized table with necessary information
def initilize_table(session):
	api_url = 'https://api.tfl.gov.uk/bikepoint'

	try:
		r = requests.get(api_url)
		data = json.loads(r.text)

		for i in range(len(data)):
			bikestation_id = data[i]['id'].lower()
			common_name = data[i]['commonName'].lower()
			terminal_id = data[i]['additionalProperties'][0]['value']

			add_station = Table(bike_id=bikestation_id, common_name=common_name, terminal_id=terminal_id)
			session.add(add_station)

		session.commit()
	except:
		print("API is not reachable.")
	pass

if __name__=="__main__":
	engine = connect_with_database()
	create_table(engine)
	session = create_session(engine)
	initilize_table(session)
	pass