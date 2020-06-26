import urllib
import requests
import json
import mysql.connector
from mysql.connector import Error

DB_NAME = 'BikePoints'
cnx = mysql.connector.connect(user='root',password='1234')
cursor = cnx.cursor()

cursor.execute("USE {}".format(DB_NAME))

data = requests.get('https://api.tfl.gov.uk/bikepoint')
bike_data=data.json()

# print(type(bike_data))

for bd in bike_data:
    id = int(bd['id'].split('_')[-1])
    name = str(bd['commonName'])
    aP = bd['additionalProperties']
    installed = aP[1]['value']
    locked = aP[2]['value']
    # instD = aP[3]['value']
    # installedDate = instD[:4]+'-'+instD[4:6]+'-'+instD[6:8]+'T'+instD[8:10]+':'+instD[10:12]+':'+instD[12:14]
    TimeSnap = aP[0]['modified'][:-5]
    NbBikes = int(aP[6]['value'])
    NbEmptyDocks = int(aP[7]['value'])
    lat = str(bd['lat'])
    long = str(bd['lon'])

    try:
        sql = 'REPLACE INTO bikes_availability (bikeid, nam, lat, longitude, installed, locked, nbBikes, nbEmptyDocks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (id, name, lat, long, installed, locked, NbBikes, NbEmptyDocks)
        cursor.execute(sql, val)
        cnx.commit()
        sql = 'REPLACE INTO timestamp_bikes_data (bikeid, nam, lat, longitude, installed, locked, TimeSnap, nbBikes, nbEmptyDocks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (id, name, lat, long, installed, locked, TimeSnap, NbBikes, NbEmptyDocks)
        cursor.execute(sql, val)
        cnx.commit()
    except Error as e:
        print('Error: ', e)

cursor.close()
cnx.close()


