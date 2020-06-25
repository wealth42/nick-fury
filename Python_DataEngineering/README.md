Requirements:
-------------------
1.Python Compiler
2.MySql Server
3.Packages used in this assignment:mysql connector,schedule,datetime,requests.

How To Run:
-----------------------------------------------------------

1.In project.py file in main method database configuration method,creating tables method are called.scheduler module is used 
to schedule the script every 5 minutes.

2.Methods defined:

	1.database_config()- it configures the database connectivity and returns db,mycursor references.
	
	2.create_table(db,mycursor)-it creates tables[bikes_available1(dock_point,no_of_bikes,timestamp,date),
	timestamps_table1(timestamp,nof_of_bikes,dock_point,date)]

	3.api()- This method requests the api,and converts into json format and calls the methods to find  nof bikes 
		available in dockpoints ,as well as in time stamps.
		This method aslo calls a method which  inserts these required values into database.
		This method also calls query_from_users to allow users to fetch from database.
	
	4.bike_availability_at_doctpoint(list_of_json)-This method returns  no of available bikes per particular dockpoint 
		as a key value pair,key-docking point,value-[nof of bikes,timestamp,date]

	5.bike_availabilty_at_timestamp(list_of_json)- This method returns nof of bikes available in docking point in that 
		particular time stamp in form of key value pair.key-timestamp,value-[nof_of_bikes,dockingpoint,date]

	6.insert_into_database(dict_of_available_bikes,dict_of_timestamps,db,cursor)-Method for inserting required details
		 into database .

	7.query_from_users(db,mycursor)-It will fetch no of bikes available in that particular dockpoint  and timestamp accordind
		 to user's input.
		 It will fetch nof of bikes ,as well as at which dockpoint bikes are available in that particular timestamp 
		 according to the user input's.
3.Time Complexity of the program is O(N^2) .
