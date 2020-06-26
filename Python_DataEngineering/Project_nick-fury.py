# author :- Harsh Vardhan 
from datetime import datetime
import pandas as pd
import json
import requests
import mysql.connector as mysql
import schedule
import time

def activity ():
        url = "https://api.tfl.gov.uk/bikepoint" 
        response = requests.get(url)
        data = pd.DataFrame(json.loads(response.text))
        data['time'] = datetime.now()
        data.drop(['url','$type','placeType','children','childrenUrls'],axis=1,inplace=True)
        data2=[]
        data3=[]
        data4=[]
        for _ in data['additionalProperties']:
                for i in _:
##                   print(type(i))
                        if i['key'] == "NbBikes":
                                data2.append(int(i['value']))
                        if i['key'] == "NbDocks":
                                data4.append(int(i['value']))
                        if i['key'] == "Locked":
                                data3.append(str(i['value']))
        data['NbBikes'] = data2#tells number of available bikes
        data['Locked'] = data3#tells the location is locked or not although it is mostly false at location it is assumed that it could change in future hence added.
        data['NbDocks'] = data4 # it tells about the number of docks available in the area as they might change with time which changes the availability of the bikes.
        data.drop(['additionalProperties'],axis=1,inplace=True)
#      data.to_csv('my_csv.csv')
        db = mysql.connect(user='root', password='password',host='localhost', database='database_name')
        cursor = db.cursor()

        for j,row in data.iterrows():
            cursor.execute("insert into data values(" +"\""  + str(row['id']) + "\"" + "," + "\"" + str(row['commonName']) + "\"" + "," + str(row['lat']) + "," + str(row['lon']) + "," + "\"" + str(row['time']) + "\"" + "," + row['NbBikes']+"," + str(row['Locked']) + ","+row['NbDocks']");" )
        db.commit()
        cursor.close()
        db.close()

if __name__=="__main__":
    schedule.every(5).minutes.do(activity)#schedule to run the script every 5 minutes.
    while True:
        schedule.run_pending()
        time.sleep(1)

