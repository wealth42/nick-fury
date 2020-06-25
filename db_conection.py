import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from db_secrets import USERNAME, PASSWORD, PORT, DATABASENAME

# MySQL server connection
# change the USERNAME, PASSWORD, PORT & DATABASENAME 
# according to your configuration
PATH = "mysql+pymysql://{}:{}@localhost:{}/{}".format(
    USERNAME, PASSWORD, PORT, DATABASENAME
)

engine = create_engine(PATH, echo=True)
Session = sessionmaker(bind=engine)

# importing the ORM
from model import LondonBikes

def add_update_data(id: str, name: str, lat: float, lon: float, time, NbBikes: int, NbDocks: int):
    session = Session()
    try:
        # create LondonBikes object (ORM)
        bikes = LondonBikes(
            bikepoint_id = id,
            name = name,
            latitude = lat,
            longitude = lon,
            time = time,
            NbBikes = NbBikes,
            NbDocks = NbDocks
        )

        session.add(bikes)
        session.commit()
    except IntegrityError:
        # this else block is executed if the data already exists
        # rollbacking to previous state of the session
        session.rollback()

        bikes = session.query(LondonBikes).filter(LondonBikes.bikepoint_id==id).update({
            LondonBikes.NbDocks : NbDocks,
            LondonBikes.NbBikes : NbBikes,
            LondonBikes.time : time
        }, synchronize_session=False)

        session.commit()

def fetch_data(common_name):
    session = Session()

    results = session.query(LondonBikes).filter(
        LondonBikes.name.in_(common_name)
    ).all()

    entries = list()
    
    for result in results:
        entries.append({
            "bikepoint_id": result.bikepoint_id,
            "name" : result.name,
            "latitude" : result.latitude,
            "longitude": result.longitude,
            "time" : result.time.strftime("%Y-%m-%d %H:%M:%S"),
            "NbBikes" : result.NbBikes,
            "NbDocks" : result.NbDocks
        })
    
    return entries