from sqlalchemy import create_engine
from mysql_details import *
import requests
import pandas as pd
import sys

#Load data into Database
def load(df):
    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}/bikepoints".format(Username,Password,Host))
        df.to_sql(name="bikepoints data", con=engine, index=False, if_exists="replace")
        conn=engine.connect()
        conn.execute("""ALTER TABLE `bikepoints data` 
                        CHANGE COLUMN `ID` `ID` BIGINT NOT NULL PRIMARY KEY,
                        CHANGE COLUMN `Name` `Name` TEXT NOT NULL;
                        """)
    except Exception as e:
        print(e)


#Extract Data from API
def extract_load():
    url = "https://api.tfl.gov.uk/bikepoint"
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        sys.exit()
    data = response.json()

    d = []
    for bikepoint in data:
        _id = bikepoint["id"][11:]  #"id" keys in the api have value like "BikePoints_1" so storing only integer part which starts from 11th index.
        name = bikepoint["commonName"]
        latitude = bikepoint["lat"]
        longitude = bikepoint["lon"]
        for i in bikepoint["additionalProperties"]:
            if i["key"] == "Locked":
                lockedStatus = i["value"]
            elif i["key"] == "NbBikes":
                availablebikes = i["value"]
                lastupdated = str(pd.to_datetime(i["modified"][:len(i["modified"]) - 4]))
            elif i["key"] == "NbEmptyDocks":
                emptydocks = i["value"]
            elif i["key"] == "NbDocks":
                totaldocks = i["value"]

        d.append([int(_id), name, lockedStatus, int(totaldocks), int(availablebikes), int(emptydocks), float(latitude),
                  float(longitude), pd.to_datetime(lastupdated)])

    df = pd.DataFrame(d,columns=['ID', 'Name', 'Locked', 'Total Docks', 'Available Bikes', 'Empty Docks', 'Latitude',
                                   'Logitude', 'Last Update'])

    df=df.sort_values(by="ID")

    load(df)


if __name__=="__main__":
    extract_load()


