import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import database_credentials as dc
from table_skeleton import Base,Table

### database connection
def connect_with_database():
	path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(dc.USER_NAME,dc.USER_PASS,dc.DATABASE_PORT,dc.DATABASE_NAME)
	engine = sqlalchemy.create_engine(path)
	return engine


### session variable to make changes
def create_session(engine):
	Session = sqlalchemy.orm.sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	return session


### take input from user
def get_input():
	text = str(input("Enter place name to search for bike :"))
	text = text.lower()
	return text


### function to search and display results
def get_search(text,session):
	search = "%{}%".format(text)
	records = session.query(Table).filter(Table.common_name.like(search)).all()

	print("Total Match Cases Found = "+str(len(records)))
	for record in records:
		print("-----------------------------------")
		print("Common Name: "+str(record.common_name))
		print("Terminal ID : "+str(record.terminal_id))
		print("Available Bikes : "+str(record.bike))
		print("Empty Docks : "+str(record.empty_docks))
		print("Total Docks : "+str(record.total_docks))
		print("Update Time : "+str(record.update_time))
		print("Update Date : "+str(record.update_date))
	pass


if __name__=="__main__":
	engine = connect_with_database()
	session = create_session(engine)
	text = get_input()
	get_search(text,session)
	pass