# Data Engineering Challenge (Wealth 42)
> The goal of this challenge is to test your familiarity with concepts in Python and Data Engineering

## The Challenge 
- Use the bikepoint API to extract information on bike availability on various bike stands. [BikePoint API](https://api-portal.tfl.gov.uk/docs)
- Design DDLs for -
    - storing the real-time bike availability data across London
    - storing the bike availability across London across different time snapshots
- Implement these DDLs and create table(s) in MySQL for the schemas.
- Write script in Python to query this data source and update both databases accordingly
- Schedule this script to run every 5 minutes


## My Workflow
1. Creating an Environment on my local PC
2. Activating the Environment and installing necessary packages 
3. Exploring the BikePoint API using [Postmann](https://www.postman.com/#:~:text=Postman%20is%20a%20collaboration%20platform,can%20create%20better%20APIs%E2%80%94faster.) and gaining insights on the data.
4. Cloning the [directory](https://github.com/wealth42/nick-fury).
5. Setting up the Database using MySQL on my local PC.
6. Setting up the Flask Application and connecting to the Database.
7. Finally, Code !

## Instructions
> Follow the below instructions to run the code on your computer

#### 1. Requirements:

Before starting, it is mandatory to have Python and Anaconda installed on your PC.

[Download Python](https://www.python.org/downloads/) 

[Download Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

To check it installation, open command prompt and run the following 2 commands:

``` python --version ```
``` conda --version```

#### 2. Creating the Environment

Open command prompt and navigate to the desired folder where you want to save the project.

Use ```cd ``` for navigation in Windows.

Run the following command to create an environment by the name ```bike_point_env```:

``` conda create -n bike_point_env python=3.6```.

Activate the env:

``` activate bike_point_env	```.

#### 3. Installing the packages

Run the folowing command to Install all the necessary packages required to run the Project.

``` pip install requirements.txt```.

#### 4 . Setting up our Database

Its is mandatory to have MySQL installed on the computer to run the Database Server.

[Download MySQL](https://dev.mysql.com/downloads/installer/)

Once you setup the Server note down the "Username", "Passoword".

Open ```script.py, data.py``` file in an editor and change the _User_ and _Password_ fields.

##### _The setup is now Complete_ ! 

Moving on with the execution

#### 4. Run the setup.py file

Open command prompt, navigate to the project folder. Activate the environment if not done earlier.

Run the following command to create Database: "local_database" with Table "info":

```python setup.py```

#### 5. Run the main.py File

Run the main file :

``` python main.py```

If everything is executed correctly The Flask application will run on http://127.0.0.1:5000.

The webpage will display latest information of the Available Bikes across all the locations along with the time.

Also, you can check the database which will run the python script every 5 minutes.


