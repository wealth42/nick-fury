from sqlalchemy import Column, Integer, String, Float, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LondonBikes(Base):
    __tablename__ = 'bikes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    bikepoint_id = Column(String(16))
    name = Column(String(length=80))
    latitude = Column(Float)
    longitude = Column(Float)
    time = Column(DateTime)
    NbBikes = Column(Integer)
    NbDocks = Column(Integer)
    __table_args__ = (UniqueConstraint('bikepoint_id', 'time'),)

    def __repr__(self):
        return "<Bikes(name={}, latitude={}, longitude={})>".format(
            self.name, self.latitude, self.longitude
        )