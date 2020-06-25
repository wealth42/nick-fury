# -*- coding: utf-8 -*-
import requests
import mysql.connector
import schedule
import time
import datetime


# A method creating database connection
def database_config():
    db=mysql.connector.connect(host="localhost", user="root", passwd="1234",database="base")
    cursor1=db.cursor(buffered=True)
    return((db,cursor1))

# Method for creating tables[bikes_available1(dock_point,no_of_bikes,timestamp,date),timestamps_table1(timestamp,nof_of_bikes,dock_point,date)]
def create_table(db,mycursor)    :
    mycursor.execute("create table bikes_available1 (dock_point varchar(100),no_of_bikes numeric,timestamp varchar(100),date varchar(50))" )
    mycursor.execute("create table timestamps_table1(timestamp varchar(20),nof_of_bikes numeric,dock_point varchar(100),date varchar(50))")
    
# Method for inserting data into database 
def insert_into_database(dict_of_available_bikes,dict_of_timestamps,db,cursor)    :
    sql_statement1="insert into bikes_available1 values(%s,%s,%s,%s)"
    sql_statement2="insert into timestamps_table1 values(%s,%s,%s,%s)"
    for keys in dict_of_available_bikes:
        val=(keys,dict_of_available_bikes[keys][0],dict_of_available_bikes[keys][1],dict_of_available_bikes[keys][2])
        mycursor.execute(sql_statement1,val)
    
    for keys in dict_of_timestamps:
        val=(keys,dict_of_timestamps[keys][0],dict_of_timestamps[keys][1],dict_of_timestamps[keys][2])
        mycursor.execute(sql_statement2,val)
    db.commit()    

# A method using which a user can query 
def query_from_users(db,mycursor)   :
    print("Enter the dockpoint name  and the timestamp ")
    dockpoint=input()
    timestamp=input()
    x=datetime.datetime.now()
    date=str(x.date())
    # It will fetch no of bikes available as per the dockpoint name and timestamp user inputs's.
    sql_statement="select no_of_bikes from bikes_available1 where dock_point=%s and timestamp=%s and date=%s"
    mycursor.execute(sql_statement,(dockpoint,timestamp,date))
    result=mycursor.fetchone()
    print(result)
    
    #It will fetch nof of bikes ,as well as at which dockpoint bikes are available according to the timestamp user input's.
    print("Enter the timestamp to get the available bikes at that moment ")
    sql_statement1="select nof_of_bikes,dock_point from timestamps_table1 where timestamp= %s and date=%s"
    timestamps=input()
    mycursor.execute(sql_statement1,(timestamps,date))
    bikes_at_dock_points=mycursor.fetchall()
    for i in bikes_at_dock_points:
        print(i)
    
    
# This method returns  no of available bikes per particular dockpoint as a key value pair
#key-docking point,value-[nof of bikes,timestamp,date]
def bike_availability_at_doctpoint(list_of_json):
    total_no_of_bikes=0
    dict_of_available_bikes={}
    for dicts in list_of_json:
        for keys in dicts["additionalProperties"]:
            if keys["key"]=="NbBikes":
                if dicts["commonName"] not in dict_of_available_bikes:
                    dict_of_available_bikes[dicts["commonName"]]=[]
                
                dict_of_available_bikes[dicts["commonName"]].append(int(keys["value"]))
                dict_of_available_bikes[dicts["commonName"]].append((keys["modified"][11:-1]))
                dict_of_available_bikes[dicts["commonName"]].append((keys["modified"][:10]))
                
                
                total_no_of_bikes+=int(keys["value"])
    return dict_of_available_bikes
                
    
# This method returns nof of bikes available in docking point  in that particular time stamp in form of key value pair.
#key-timestamp
#value-[nof_of_bikes,dockingpoint,date]
def bike_availabilty_at_timestamp(list_of_json):
    
    dict_of_timestamps={}
    for dicts in list_of_json:
        for keys in dicts["additionalProperties"]:
            if keys["key"]=="NbBikes":
                timestamps=keys["modified"][11:-1]
                if timestamps not in dict_of_timestamps:
                    dict_of_timestamps[timestamps]=[]
                    
                dict_of_timestamps[timestamps].append(int(keys["value"]))
                dict_of_timestamps[timestamps].append(dicts["commonName"])
                dict_of_timestamps[timestamps].append(keys["modified"][:10])
    return dict_of_timestamps

# This method requests the api,and converts into json format and calls the methods to check the nof bikes available in dockpints ,as well as in time stamps.
#This method aslo calls a method which  inserts these required values into database    
# This method also calls query_from_users to allow users to fetch from database
def api():
    response=requests.get("https://api.tfl.gov.uk/bikepoint")#Extracting  API
    list_of_json=response.json()#converting into json format
    dict_of_available_bikes=bike_availability_at_doctpoint(list_of_json)
    dict_of_timestamps=bike_availabilty_at_timestamp(list_of_json)
    insert_into_database(dict_of_available_bikes,dict_of_timestamps,db,mycursor)
    query_from_users(db,mycursor)
    
        
        
if __name__=="__main__":
    db,mycursor=database_config()
    create_table(db,mycursor)
    api()
    # scheduler module schedules to run this script evrery 5 minutes.
    schedule.every(5).seconds.do(api)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    
    

