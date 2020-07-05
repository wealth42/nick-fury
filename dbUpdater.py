import requests
import pandas as pd
from sqlalchemy import create_engine
import pymysql


def script():
    try:
        result = requests.get('https://api.tfl.gov.uk/bikepoint')

        engine = create_engine('mysql+pymysql://#username:#password@localhost:3306/bikepoint')
        connection = engine.connect()

        bike_data = pd.DataFrame(result.json()).drop(columns=['$type', 'childrenUrls', 'children'])
        print (type(bike_data['additionalProperties'][0][0]))
        size = len(bike_data)
        additional_properties = bike_data['additionalProperties']
        bike_data = bike_data.drop(columns=['additionalProperties'])
        docks, bikes, spaces = [], [], []
        for i in range(size):
            for p in additional_properties[i]:
                key = (p.get('key'))
                if key == 'NbDocks': docks.append(p.get('value'))
                if key == 'NbBikes': bikes.append(p.get('value'))
                if key == 'NbEmptyDocks': spaces.append(p.get('value'))
        bike_data['docks'] = docks
        bike_data['bikes'] = bikes
        bike_data['spaces'] = spaces
        bike_data.to_sql('table', connection, if_exists='replace')


    except Exception as err:
        print('found error', err.with_traceback())
        exit(0)


if __name__ == '__main__':
    script()
