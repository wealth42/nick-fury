from sqlalchemy import  Table, Column, Integer, String,Date,Time,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class table_structure(Base):
    __tablename__='bikepoint_table'
    bike_id = Column(String(30),primary_key=True)
    name_of_loaction=Column(String(100))
    latitude= Column(Float)
    longitude= Column(Float)
    available_bikes= Column(Integer)
    empty_docks=Column(Integer)
    total_docks=Column(Integer)
    date_of_update= Column(Date)
    time_of_update = Column(Time)
	
            
