from sqlalchemy import Column, Integer, String, Float, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LondonBikes(Base):
    __tablename__ = 'bikes'

    id = Column(String(16), primary_key=True, unique=True)
    name = Column(String(length=80))
    latitude = Column(Float)
    longitude = Column(Float)
    time = Column(Time)
    NbBikes = Column(Integer)
    NbDocks = Column(Integer)

    def __repr__(self):
        return "<Bikes(name={}, latitude={}, longitude={})>".format(
            self.name, self.latitude, self.longitude
        )