# Submission by Debdut Goswami

Kindly follow the steps below to sucessfully run the files.

## INSTRUCTIONS

1. (pre-requisite) have python3 and MySQL server installed.

2. create a virtual enviornment by typing the following

    <pre>python3 -m venv env</pre>

    Now activate the environment by typing

    <pre>source env/bin/activate</pre>

3. To install all the packages, type

    <pre>pip intall -r requirements.txt</pre>

    If you encounter an error while installing <em>mysqlclient</em> then you need to run the bellow command and then re-run the pip install.

    <pre>sudo apt-get install python3-dev default-libmysqlclient-dev build-essential</pre>

4. Now, you need to create a database in your MySQL server. After the database is created, export the MySQL server username, password, port on which it is running and the database name just created. To do so, <pre>export db_username=yourdatabaseusername
export db_password=yourdatabasepassword
export db_port=portnumber
export db_name=yourdatabasename</pre>

5. To create the table, run the <strong><u>create_db.py</u></strong> file by typing, <pre>python create_db.py</pre>

6. Next, create a cron job and it will run the <strong><u>fetch.py</u></strong> file every 5 minutes. To  do that, open up the terminal and type <pre>crontab -e</pre> and it should open up a file. Add the below line to make it execute every 5 minutes. <pre>*/5 * * * * python3 /path/to/nick-fury/fetch.py</pre>
    In case you are having difficulty in setting up the cron job, I have also added a file called <strong><u>cron.py</u></strong>. Just export the enviornment variables. To do so, type <pre>export path_fetch=/path/to/fetch.py</pre>

    Note:
     You need to have all the python modules installed globally too and not only in the virtual environment for the cron jobs to execute successfully.


7. Now, our job is scheduled. Now, simply run the <strong><u>app.py</u></strong> file and then open up your browser and go to [http://localhost:5000/](http://localhost:5000/) to see the data stored in the database.
