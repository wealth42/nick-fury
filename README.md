### Instruction to run 

I hope you have already installed python3.X and MySQL in host system. And install necessary plugins for communicate with mysql server.

### Assumption
1. every bike-stands are permanent. There is no temporary installed bike-stand.

### 1. Necessary changes made by user in file.
first you have to change ```database_auth.py``` to select database, user and password for that user.

### 2. First run.
run ```create_database.py``` file. this will create tables in selected database.

### 3. Initialize values
now, run ```update_database.py``` file that is update database table with current values on API.


### set-up cronjob for run script every 5 min. 
open terminal.
run command ```crontab -e```.
After open editor, paste or write this command in that file.
 ```*/5 * * * * python3 /path/to/update_database.py```
save file and exit.


### user search
user can search for available bikes at specific place by entering place name or subset of place name.
for this, run ```search.py``` file and follow ahead.