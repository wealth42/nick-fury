import requests
from datetime import datetime
from db_conection import add_update_data

DOMAIN_URI = 'https://api.tfl.gov.uk/bikepoint'

def fetch_data_from_api():
    try:

        response = list(requests.get(DOMAIN_URI).json())

        for info in response:
            _id = info['id']
            _commonName = info['commonName']
            _lat, _long = float(info['lat']), float(info['lon'])

            for item in info['additionalProperties']:
                if item['key'] == 'NbBikes':
                    _NbBikes = int(item['value'])
                elif item['key'] == 'NbDocks':
                    _NbDocks = int(item['value'])

                try:
                    _time = datetime.strptime(
                        item['modified'][:-1], '%Y-%m-%dT%H:%M:%S.%f'
                    )
                except ValueError:
                    _time = datetime.strptime(
                        item['modified'][:-1], '%Y-%m-%dT%H:%M:%S'
                    )

            # adding or updating depending on
            # existance of the data in the table
            add_update_data(
                _id, _commonName, _lat, _long, _time, _NbBikes, _NbDocks
            )
            
    except Exception as E:
        print(E)


if __name__ == "__main__":
    fetch_data_from_api()