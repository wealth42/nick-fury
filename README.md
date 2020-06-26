### Instruction to run 

I hope you have already installed python3.X and MySQL in host system. And install necessary plugins for communicate with mysql server.

### Assumption
1. every bike-stands are permanent. There is no temporary installed bike-stand.

run below command for installing dependancy of projects.
```pip3 install -r requirements.txt```

### 1. Export user database credentials into environment variables.
```
export db_user_name=your_database_username
export db_user_pass=your_database_password
export db_name=your_database_name
export db_port=database_port(default_value:3306)
```

### 2. First run.
run ```create_database.py``` file. this will create tables in selected database.

### 3. Initialize values
now, run ```update_database.py``` file. It is update database table with current values on API.


### set-up cronjob for run script every 5 min. 
open terminal.
run command ```crontab -e```.
After open editor, paste or write this command in that file.
 ```*/5 * * * * python3 /path/to/update_database.py```
save file and exit.


### user search
user can search for available bikes at specific place by entering place name or subset of place name.
for this, run ```search.py``` file and follow ahead.