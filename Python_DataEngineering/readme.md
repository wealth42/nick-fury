How to 	Run the Scripts:
----------------------------------

1.In "Extract_Store_Fetch.py" module a main method is defined under which all the method starting from configuring of Mysql Database to fetching the data from Mysql DB is defined.

2. Methods defined in "Extract_Store_Fetch.py":
	a.bikesPerBikePoint(json_data)--> this function takes json object as input and traverses whole the API List and returns the json object having key BikePointName and list of its properties such as datetime,bikesavailble. Ex of returned json object {"Marathalli":[120,"2020-06-25--02:34"]} where key is bikepoint names ,value 120 represent the no of bikes available and other one is the timestamp
	
	b.bikesPerTimeSnapShot(json_data)-->this function takes json object as input and function traverses the API List and returns  the Total No. of Bikes available across London including all the BikePoints at a particular Point of Time. Ex of returned object {"2020-06-25--02:34":120}, key is time stamp and value is no of bikes available across london including all bike points.

	c.databaseConfig()--> function configures the DataBase connectivity, returns the cursor and db references.

	d.databaseInsert(cursor,db,time_snap_shot_bike_data,bikepointdetails) --> this function takes curson , db and the json objects returned by "bikesPerBikePoint" and "bikesPerTimeSnapShot" as input and  inserts all the required values from API into two table, using sql1 table we will insert bikepointname, no of available bikes, datetime, using sql2 table we will insert total no of bikes present at a particular timesnapshot.

	e.databaseFetch(cursor,db,select,current_datetime_in_IST_string)--> This function takes the input provided by the User i.e the bike point name to fetch the no of bikes available at the time of searching.
	
	f.createTables(): This function will create required tables only once and after that the above methods will be called in every 5 minutes except this method and fetch method.

3. All the functions are written separately and there is no code redundat , and if you go through the code , i have used the code reusability property to convert the time from UTC to IST. 

4. Time Complexity of above Program is O(N^2) and space Complexity is O(2*N)

5.The whole program takes 5 seconds to execute everything including extracting , Storing and Fetching the requried data once in every five minutes.


    

     

