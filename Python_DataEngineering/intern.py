import requests,os
import json
import mysql.connector
from mysql.connector import Error

DB_NAME = 'BikePoints'
user = os.environ.get('USER')
password = os.environ.get('password')
cnx = mysql.connector.connect(user=user, password=password)
cursor = cnx.cursor()

cursor.execute("USE {}".format(DB_NAME))

data = requests.get('https://api.tfl.gov.uk/bikepoint')
bike_data = data.json()

for bd in bike_data:
    id = int(bd['id'].split('_')[-1])  #id is like BikePoints_1. To take the last number, '-1' index is used.
    name = str(bd['commonName'])
    aP = bd['additionalProperties']
    for prop in aP:
        if prop['key'] == 'Installed':
            installed = prop['value']
        if prop['key'] == 'Locked':
            locked = prop['value']
        if prop['key'] == 'NbBikes':
            NbBikes = int(prop['value'])
        if prop['key'] == 'NbEmptyDocks':
            NbEmptyDocks = int(prop['value'])
    TimeSnap = aP[0]['modified'][:-5]  #this uses the modified property which is common in all the additional propertied. Hence, 0 will work even if structure is changed.
    lat = float(bd['lat'])
    long = float(bd['lon'])

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


