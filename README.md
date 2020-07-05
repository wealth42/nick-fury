# Assumption
1. All bikes are fully functional , data given is accurate.

# Requirements
1. Python 3
2. Mysql 

# How to run

## first run the ddl sql script provided as DDL.sql
To run the sql script file just paste this command in command promt 
> mysql -u yourusername -p yourpassword  < DDL.sql
or just simply use mysql workbench and load this script and press execute button

## second run the python code
### run the updating script
in this file change your username and password for mysql
then using python compiler run the given cron.py file and add your username and absolute path to dbUpdater in the variable mentioned in the file.
which is a script which once executed will update the database(created in upper step) every 5 minutes until program terminated.

*  To Schedule the python script to run at every 5 minutes in windows we use Task Scheduler

		* Open the Task Scheduler

		* Now Click on Create Task Which Will be present  in th right-hand panel named Action

		* A window will open .
		
		* First You need to type the name of schduler (of your choice).

		* Now click on Action Tab shown in window .Then click on new .After that in the input box named Program/Scripts you need to set the location of Python.exe installed in your pc . Then you have to enter the file name ```dbUpdater.py``` in the input box named add arguments.Then you have to enter the path of ``` dbUpdater.py``` this file located in your pc in the input box named  start in. Then click ok.

### run queries on location
then run the query.py file which will ask to input a string(any subset of commonName) to be searched for checking the availability of bikes at locations.

