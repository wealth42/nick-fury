import requests
from datetime import datetime
from dateutil import tz
import mysql.connector
import schedule
import time

#dataBaseConfig function configures the DataBase connectivity, returns the cursor pointing to the database 
def databaseConfig():
    database = "bikeapi"
    username = 'root'
    password = 'XXXkalia@123'

    # Open database connection
    db = mysql.connector.connect(host='localhost', user=username, passwd=password, db=database)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    return (cursor,db)

#This function converts UTC Time provided in API to IST using Python package dateutil and return the IST date and time as a String
def convertTOIST(datetime_in_UTCs):
    from_zone = tz.tzutc() #as we know the given timezone is in UTC
    to_zone = tz.tzlocal() #here it finds out the local time standard
    try:
        datetime_in_UTC=datetime.strptime(datetime_in_UTCs,'%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        datetime_in_UTC=datetime.strptime(datetime_in_UTCs,'%Y-%m-%dT%H:%M:%SZ')
        
    UTC=datetime_in_UTC.replace(tzinfo=from_zone) #it makes the incoming datetime as UTC whatever the standard may be
    datetime_in_IST = UTC.astimezone(to_zone) #it makes it to IST
    IST=str(datetime_in_IST.hour)+":"+str(datetime_in_IST.minute)
    return str(datetime_in_IST.date())+"--"+IST


#bikesPerBikePoint function traverses whole the API List and returns and prints the json object having key BikePointName and list of its properties such as datetime,bikesavailble
def bikesPerBikePoint(json_data):
    BikePointDetails={}
    for bikedata in json_data: #traversing all the json Objects present in API List
        for properties in bikedata["additionalProperties"]: #here i am traversing json object present inside additionalProperties to check "Key" as "NbBikes" if it is available i am trying to extract the value associated with that key
            if properties["key"] == "NbBikes":
                IST=convertTOIST(properties["modified"])  #It passes the UTC Time as a String to convertTOIST function and gets IST Date and time as a String
                bikepointname=bikedata["commonName"]
                datetime=IST
                noofbikes=properties["value"]
                BikePointDetails[bikepointname]=[noofbikes,datetime]
                #print("Bike Point Name: "+bikepointname)
                #print("No oF Bikes Available: "+noofbikes)
                #print("Date: "+IST)
                #print(" ")
    return BikePointDetails

#bikesPerTimeSnapShot function traverses the API List and returns  the Total No. of Bikes available across London including all the BikePoints at a particular Point of Time
def bikesPerTimeSnapShot(json_data):
    timing_snap_shot={}
    for bikedata in json_data:
        for properties in bikedata["additionalProperties"]:
            if properties["key"] == "NbBikes":
                IST=convertTOIST(properties["modified"]) #this function converts UTC to IST and returns the result as a String
                if IST not in timing_snap_shot:
                    timing_snap_shot[IST]=int(properties["value"])
                else:
                    timing_snap_shot[IST]+=int(properties["value"])
    return timing_snap_shot


#This function inserts all the required values from API into twoo table
#using sql1 table we will insert bikepointname, no of available bikes, datetime
#using sql2 table we will insert total no of bikes present at a particular timesnapshot
def databaseInsert(cursor,db,time_snap_shot_bike_data,bike_point_details):
    sql1="insert into Bike_Detail(bikepointname, noofbike, datetime) VALUES (%s, %s, %s)"

    #inserting into Total_Bike_Table using sql2
    sql2="insert into time_snap_shot_detail(datetime, noofbike) VALUES (%s, %s)"
    for date_time in time_snap_shot_bike_data:
        datetime=date_time
        no_of_bikes=str(time_snap_shot_bike_data[date_time])
        value=(datetime,no_of_bikes)
        cursor.execute(sql2,value)
        db.commit()
        
    
    
    #inserting into Bike Table using sql1
    for bikepoint in bike_point_details:
        bikepointname=bikepoint
        noofbikes=bike_point_details[bikepoint][0]
        datetime=bike_point_details[bikepoint][1]
        value=(bikepointname,noofbikes,datetime)
        cursor.execute(sql1,value)
        db.commit()
        
    
     
#this function will fetch no of bikes available as per user's selection of bikepointname and currenttime
def databaseFetch(cursor,db,select,datetime):
    sql="select noofbike from Bike_Detail where bikepointname= %s and datetime= %s"
    value=(select,datetime,)
    cursor.execute(sql,value)
    result=cursor.fetchall()
    if cursor.rowcount == 0:
        print("No Bikes available at this point of Time")
    else:
        for each_row in result:
            print(select+" : "+each_row[0])
            
 #creates the required table           
def createTables(cursor,db):
    sql1="create table Bike_Detail(bikepointname varchar(255),noofbike varchar(255),datetime varchar(255))"
    sql2="create table time_snap_shot_detail(datetime varchar(255),noofbike varchar(255))"
    cursor.execute(sql1)
    db.commit()
    cursor.execute(sql2)
    db.commit()
    
    
        

#This executes as a main function where the subfunction are called
def modules(cursor,db):
    bikepointdetails=bikesPerBikePoint(json_data)
    time_snap_shot_bike_data=bikesPerTimeSnapShot(json_data)
    databaseInsert(cursor,db,time_snap_shot_bike_data,bikepointdetails)


    
if __name__ == "__main__":
    request=requests.get("https://api.tfl.gov.uk/bikepoint") #here i am extracting the API using get method
    json_data=request.json() #converting the request object to JSON so as to extract the relevant Data
    tuples=databaseConfig()
    cursor=tuples[0]
    db=tuples[1]
    createTables(cursor,db)
    schedule.every(5).minutes.do(modules,cursor,db)
    #for Fetching details as per user bike point choice to know the no of bikes available
    #we can disable the comment line and run whenever we need it, this is a extra functionality we have added 
    """
    select=input("Enter the BikePoint name to fetch the no of bikes available")
    current_datetime_in_IST=datetime.now()
    current_datetime_in_IST_string=str(current_datetime_in_IST.date())+"--"+str(current_datetime_in_IST.hour)+":"+str(current_datetime_in_IST.minute)
    databaseFetch(cursor,db,select,current_datetime_in_IST_string)
    """
    
    while True: 
        # Checks whether a scheduled task  
        # is pending to run or not 
        schedule.run_pending()
        time.sleep(100)
    
    
    
    
    
  
    

            