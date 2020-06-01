from datetime import datetime
import pandas as pd
import json
import requests
import mysql.connector as mysql

url = "https://api.tfl.gov.uk/bikepoint" 
response = requests.get(url)
data = pd.DataFrame(json.loads(response.text))

data['time'] = datetime.now()
data.drop(['url','$type','placeType','children','childrenUrls'],axis=1,inplace=True)

data['NbBikes'] = data['additionalProperties'].apply(lambda x : x[6]['value'])
data.drop(['additionalProperties'],axis=1,inplace=True)

db = mysql.connect(user='root', password='',host='localhost', database='db')
cursor = db.cursor()

for ele in data.iterrows():
    row = ele[1]
    cursor.execute("insert into data values(" + 
                    "\""  + str(row['id']) + "\"" + "," + 
                    "\"" + str(row['commonName']) + "\"" + "," + 
                    str(row['lat']) + "," + 
                    str(row['lon']) + "," + 
                    "\"" + str(row['time']) + "\"" + "," + 
                    str(row['NbBikes']) +
                   ");" )
                   
db.commit()
cursor.close()
db.close()
