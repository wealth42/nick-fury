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

def getdata(li):
    for ele in li:
        if ele["key"] == "NbBikes":
            data["NbBikes"] = ele["value"]
        elif ele["key"] == "NbDocks":
            data["NbDocks"] = ele["value"]
            
data['additionalProperties'].apply(getdata)

data.drop(['additionalProperties'],axis=1,inplace=True)

data_types = {"NbBikes" : int,"NbDocks":int}
data = data.astype(data_types)

db = mysql.connect(user='root', password='',host='localhost', database='db')
cursor = db.cursor()

for idx,row in data.iterrows():
    cursor.execute("insert into data values(" +
                    "\""  + str(row['id']) + "\"" + "," +
                    "\"" + str(row['commonName']) + "\"" + "," +
                    str(row['lat']) + "," +
                    str(row['lon']) + "," +
                    "\"" + str(row['time']) + "\"" + "," +
                    str(row['NbBikes']) + "," + 
                   str(row['NbDocks']) + 
                   ");" )

db.commit()
cursor.close()
db.close()
