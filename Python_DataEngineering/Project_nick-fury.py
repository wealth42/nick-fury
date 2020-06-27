# author :- Harsh Vardhan 
from datetime import datetime
import pandas as pd
import json
import requests
import mysql.connector as mysql
import schedule
import time
from decouple import config

USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')

def activity ():
        url = "https://api.tfl.gov.uk/bikepoint" 
        response = requests.get(url)
        data = pd.DataFrame(json.loads(response.text))
        data['time'] = datetime.now()
        data.drop(['url','$type','placeType','children','childrenUrls'],axis=1,inplace=True)
        nbbikes=[]
        nbdocks=[]
        locked=[]
        for _ in data['additionalProperties']:
                for i in _:
##                   print(type(i))
                        if i['key'] == "NbBikes":
                                nbbikes.append(int(i['value']))
                        if i['key'] == "NbDocks":
                                nbdocks.append(int(i['value']))
                        if i['key'] == "Locked":
                                locked.append(str(i['value']))
        data['NbBikes'] = nbbikes # tells number of available bikes
        data['Locked'] = locked # tells the location is locked or not although it is mostly false at location it is assumed that it could change in future hence added.
        data['NbDocks'] = nbdocks # it tells about the number of docks available in the area as they might change with time which changes the availability of the bikes.
        data.drop(['additionalProperties'],axis=1,inplace=True)
#       data.to_csv('my_csv.csv')
        db = mysql.connect(user= USER, password= PASSWORD ,host= HOST, database='database_name')
        cursor = db.cursor()
        for j,row in data.iterrows():
            cursor.execute("insert into data values(" +"\""  + f"{str(row['id'])}" + "\"" + "," + "\"" + f"{str(row['commonName'])}" + "\"" + "," + f"{str(row['lat'])}" + "," + f"{str(row['lon'])}" + "," + "\"" + f"{str(row['time'])}" + "\"" + "," + f"{row['NbBikes']}"+"," + f"{row['NbDocks']}"  + ","+ f"{str(row['Locked'])}" + " );" ) 
        db.commit()
        cursor.close()
        db.close()

if __name__=="__main__":
    schedule.every(5).minutes.do(activity)#schedule to run the script every 5 minutes.
    while True:
        schedule.run_pending()
        time.sleep(1)

