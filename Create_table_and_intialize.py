from sqlalchemy import create_engine, Table, Column, Integer, String,Date,Time,Float,MetaData
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from Layout_table import Base,table_structure,history_table_structure
from requests import get
from datetime import date
from datetime import datetime
import os
now = datetime.now()
time = now.strftime("%H:%M:%S")
today = date.today()

#Create A database connection..
def database_connect():
    path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(os.getenv('User_name'),os.getenv('Password'),os.getenv('Port'),os.getenv('Db_name'))
    engine = create_engine(path)  
    return engine
#create Table
def table_create(engine):
    try:
        if not engine.dialect.has_table(engine, table_structure.__tablename__):
            Base.metadata.tables[table_structure.__tablename__].create(engine)
        else:
             print('Table {} are Already created Need Not to create again'.format(table_structure.__tablename__))


        if not engine.dialect.has_table(engine, history_table_structure.__tablename__):
             Base.metadata.tables[history_table_structure.__tablename__].create(engine)
        else:
             print('Table {} are Already created Need Not to create again'.format(history_table_structure.__tablename__))
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
        lat = x['lat']
        long = x['lon']
        for y in x['additionalProperties']:
            if y['key']=='NbBikes':
                no_bikes = y['value']
            if y['key']=='NbEmptyDocks':
                emp_docks = y['value']
            if y['key']=='NbDocks':
                tt_docks = y['value']
        result = sess.query(table_structure).filter(table_structure.bike_id.like(id_of_bike)).all()
        if len(result)==0:
            value_add = table_structure(bike_id=id_of_bike , name_of_loaction = name,latitude=lat,longitude=long,available_bikes=no_bikes,empty_docks=emp_docks,total_docks=tt_docks,date_of_update=today,time_of_update= time)
            sess.add(value_add)
        else:
            pass
    sess.commit()
        
    pass


if __name__ == '__main__':
    eng = database_connect()
    table_create(eng)
    sess = Session_create(eng)
    table_intialize(sess)
        
