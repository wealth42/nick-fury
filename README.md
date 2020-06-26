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
then using python compiler run the given bikepoint.py file 
which is a script which once executed will update the database(created in upper step) every 5 minutes until program terminated.
### run queries on location
then run the query.py file which will ask to input a string(any subset of commonName) to be searched for checking the availability of bikes at locations.

