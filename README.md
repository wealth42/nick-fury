# Follow the following steps to Execution of Program
## Prerequisite
* Need to install python3.X
* Need to install Mysql and all the plugins needed
# STEPS
* 1) Run this script ```pip install -r reqirement.txt```
* 2) Create The Enviroment Variable using following command
 * ```setx User_name "Enter Your Database user name"```
 * ```setx Password "Enter Your Database Password of that user"```
 * ```setx Port "Enter Your Database Port Number"```
 * ```setx Db_name "Enter Name of Database of your choice"```

* 3) Run the file named ``` Create_Database.py``` it will create a database if it dose not exist 

* 4) Run the script named ```Create_table_and_intialize.py``` it will create the table if it dose not exist and intialize with values

	* To Schedule the python script to run at every 5 minutes in windows we use Task Scheduler

		* Open the Task Scheduler

		* Now Click on Create Task Which Will be present  in th right-hand panel named Action

		* A window will open .

		* First You need to type the name of schduler (of your choice).

		* Now click on Action Tab shown in window .Then click on new .After that in the input box named Program/Scripts you need to set the location of Python.exe installed in your pc . Then you have to enter the file name ```Interval_update_database.py``` in the input box named add arguments.Then you have to enter the path of ``` Interval_update_database.py``` this file located in your pc in the input box named  start in. Then click ok.


		* Now click on Triggers Tab shown in the window. Then click on new . After that click Radio button daily .After that click on the check box named ```Repeat task every``` set the value to 5 minute .Then click on ok.

		* Again click on ok button.

* 5) Now you can run ```fetch_data_from_database.py``` and see the result of particular location	
