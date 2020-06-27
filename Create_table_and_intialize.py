from sqlalchemy import create_engine, Table, Column, Integer, String,Date,Time,Float,MetaData
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from Layout_table import Base,table_structure
from requests import get
import os

#Create A database connection..
def database_connect():
    path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(os.getenv('User_name'),os.getenv('Password'),os.getenv('Port'),os.getenv('Db_name'))
    engine = create_engine(path)  
    return engine
#create Table
def table_create(engine):
    try:
        if not engine.dialect.has_table(engine, table_structure.__tablename__):
            Base.metadata.create_all(engine)
        else:
            print('Table Already created Need Not to create again')
    except Exception as e:
         print(e)




         
#Establish a session
def Session_create(sess_engine):
	sess_maker = sessionmaker()
	sess_maker.configure(bind=sess_engine)
	sess = sess_maker()
	return sess



    
#Intialize the table:
def table_intialize(sess):
    url = 'https://api.tfl.gov.uk/bikepoint'
    response = get(url)
    api_data = response.json()
    for x in api_data:
        id_of_bike = x['id']
        name = x['commonName']
        result = sess.query(table_structure).filter(table_structure.bike_id.like(id_of_bike)).all()
        if len(result)==0:
            value_add = table_structure(bike_id=id_of_bike , name_of_loaction = name )
            sess.add(value_add)
        else:
            pass
    sess.commit()
        
    pass


if __name__ == '__main__':
    eng = database_connect()
    ret =table_create(eng)
    sess = Session_create(eng)
    table_intialize(sess)
        
