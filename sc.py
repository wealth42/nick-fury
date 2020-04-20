import json, requests
import sqlite3


conn = sqlite3.connect('Bike.db')
c = conn.cursor()
c.execute('CREATE TABLE if not exists realtimewithT (Id,value INTEGER, timestamp)')
c.execute('CREATE TABLE if not exists realtime (id,location, lat FLOAT, lon FLOAT)')
conn.commit()


url = "https://api.tfl.gov.uk/bikepoint"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
#print (parsed)

rn= (len(parsed))
for i in range(rn):
    Id=(parsed[0]['id'])
    location=(parsed[0]['commonName'])
    lat=(parsed[0]['lat'])
    lon=(parsed[0]['lon'])
    
    abc=(parsed[0]['additionalProperties'])[0]
    value=(abc['value'])
    timestamp=(abc['modified'])
    c.execute('INSERT INTO realtime (Id,location,lat,lon) VALUES(?,?,?,?)',(Id,location,lat,lon))
    conn.commit()
    
    c.execute('INSERT INTO realtimeWithT (Id,value,timestamp) VALUES(?,?,?)',(Id,value,timestamp))
    conn.commit()
    
    

print ("Success")
