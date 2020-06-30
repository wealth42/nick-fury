import requests
import mysql.connector
from datetime import datetime

# connecting to the server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="Wealth_BIKE"
)
mycursor = mydb.cursor()

# Getting input from the API
inp=requests.get("https://api.tfl.gov.uk/bikepoint")

#converting to json
ds=inp.json()


# In th table, i've created the column for data_time as TIMESTAMP so no need to change into time format

#Taking the from data and preprocessing it
time=[data['additionalProperties'][1]['modified'] for data in ds]
# converting to "Y-m-d H:M:S"
dt=[t[0:10]+" "+t[11:19] for t in time]

#taking bike counts
cnt=[d['additionalProperties'][6]['value'] for d in ds]

#taking place
place=[data['commonName'] for data in ds]

#if needed can be used but need to change the table
#id_0=[d['id'] for d in ds]
#url=[d['url'] for d in ds]
#commonName=[d['commonName'] for d in ds]
#Bikes=[d['additionalProperties'][6]['value'] for d in ds]
#EmptyDocks=[d['additionalProperties'][7]['value'] for d in ds]
#lat=[d['lat'] for d in ds]
#lon=[d['lon'] for d in ds]

rows=list(zip(dt, cnt, place))

#inserting into table
sql = "INSERT INTO london (date_time, bike_count, place) VALUES (%s, %s, %s)"
mycursor.executemany(sql, rows)

mydb.commit()

mycursor.close()

# appending the cron job time in the file append.txt 
myFile = open('/home/[path]/append.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))