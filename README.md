# Data Engineering challenge assignment for Wealth42

Please follow the instructions in order to run the program successfully.

Pre-requisite: Python and MYSQL server should be installed.

## INSTRUCTIONS

1. Install all the required packages by typing the following command in your command prompt
	
	<pre>pip install -r requirements.txt</pre>

2. Now store your host, username and password of your mysql server in environment variables as Host, user and Password respectively.

3. Now to create database "bikepoint" and then table "bikepoints data" inside that database run the file <strong><u>create_database.py</u></strong> by command

	<pre>python create_database.py</pre>

4. Next, to insert/update data into your database table "bikepoints data" run the file <strong><u>Extract&Load.py</u></strong> by command 
	
	<pre>python Extract&Load.py</pre>

5. Now to update data every 5 minutes, we need to schedule the file <strong><u>Extract&Load.py</u></strong> to run every 5 minutes for that follow the steps below:
   
   <strong><u>Using Crontab</u></strong>

 - Open terminal and run command "crontab" with the "-e" flag to edit the cron table

   <pre>crontab -e</pre>
 
 - Now add the following line:

   <pre>*/5 * * * * python3 /path/to/Extract&Load.py

 - Save the file, and that is it.


   <strong><u>Using Task Scheduler</u></strong>

-  Click on Start Windows, search for Task Scheduler, and open it.
-  Click "create task" at the right window, enter a name for the task and go to actions.
-  Click "New", In the Program/script field insert your python executable file path, you can get it by following command 
	
	 <pre>python -c "import sys; print(sys.executable)"</pre>
   
   then in the Add arguments field insert "Extract&Load.py" and in the start in field insert the location of "Extract&Load.py" file, then go to Triggers.
-  Click "New", Under Advanced settings panel, tick Repeat task every 5 minutes, and set Indefinitely.
-  Finally, click OK.
-  Our python script to update data every 5 minutes is scheduled. 

6. Now to query this data source run the file <strong><u>Search_places.py</u></strong> by command
	
	<pre>python Search_places.py</pre>

   This will ask you the place whose bike availability detail you want to know (you can give subset also) and it will return the details of all the matching records.
