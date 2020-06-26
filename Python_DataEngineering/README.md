1. First, MYSQL server needs to be started and running up.

2. Database.py file is used to create the database. On line 37 in Database.py, the username and password should be changed to the username and password of the running MYSQL server. This file should be executed.

3. crontab file contains the script to run the file for every 5 minutes.
It contains the line 'cd /home/harsha/Desktop/internshala/ && /usr/bin/python3 /home/harsha/Desktop/internshala/intern.py' where the first path is the path to the directory where 'intern.py' file is in. Second path is the path to python (you can use python or python3). Third path is the path to 'intern.py' file.

After editing this paths, add this line to crontab. ('using crontab -e').

Now, the tables in the database will get updated every 5 minutes.

Database and intern are the two python scripts.

Database.py
Database connects to the mysql server and creates a database 'BikePoints' and creates two tables within it.
1. bikes_availablility to store the real time bikes availability across different places in London (along with lattitude and longitude). Columns in this table are:

i bikeid,
ii name,
iii latitude,
iv longitude,
v installed (true or false),
vi locked (true or false),
vii number of bikes,
viii number of empty docks.

2. timestamp_bikes_data to store the time snapshots of the availability of bikes when each time updated. Columns in this table are:

i bikeid,
ii name,
iii latitude,
iv longitude,
v installed (true or false),
vi locked (true or false),
vii TimeSnap when the data is updated
viii number of bikes,
ix number of empty docks.

Only difference is TimeSnap. Entire data is stored at each updated timesnap.


intern.py
intern gets the data using requests and converts it into json object. Using this object, the values required to fill the tables are taken. These values are inserted into the tables.