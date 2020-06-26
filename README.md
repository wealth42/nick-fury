# nick-fury

# How to run
There is a file createdatabase.py. Run this file it will ask for password and will create databases.\
After that. you have to run cronjob.py. Again it will also ask you for password of you mysql. After enterning the password it will run in every 5 minute.\
\
There is a file called check_availability.py\
You have to run it (python check_availability "CommonName"). It will give you the latest information of no. of bikes of this place. Example is below.\
![](images/screenshot.png)

There is a file scrape.py. This is a file for all the backend operation. You don't need to run that.\

# Approach and assumption.
a. Two databases for storing real-time bike availability data and bike availability data at different time snapshot. Schema would be same for both databases.\
b. Two table in each database\
c. One table is for storing terminal id, common name, terminal name and terminal id is our primary key.
d. Second table is for storing terminal name, no. of bikes available, no. of empty docks, no. of docks, modified time. For real-time database terminal name would be our primary key and for other database (terminal,modified time) would be our primary key.\
e. Fetching data from online API in python using request module. Structuring the data.\
f. For real time database. Deleting rows which is being modified in online API and re uploading the data in database.\
g. For Other database uploading the data if it get modified in online API.\
h. Use root directory of mysql database.\

# Install
please install\
pip install mysqlclient\
pip install schedule\
pip install mysql-connector-python
