# Submission for Data Engineering challenge assignments in Wealth42

##### My setup.
  - python 3.6.8
  - Ubuntu 18.04
  - MySQL Server version: 5.7.30-0
# Installing MySQL in Ubuntu
[Instruction](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
```
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```
###### My setup
user="root"
password="password"

###  To install python requirements 
```
pip3 install -r requirements.txt 
```
# To create Database and Table!

  - Before running the file make sure there is no DB name Wealth_BIKE
  - Change user and password of DB connection
 ```
 python3 model.py
 ```
 
 # To run the API file!

  - Before running this set the path for storing file in append.txt
  - Change user and password of DB connection
 ```
 python3 run.py
 ```
 # To setup the cron job to run python script for every 5min !
To install the cron
```
sudo apt install cron
```

After installing that run below command
 ```
 crontab -e
 ```
 GNU editor opens.
 Copy paste the following command in that editor save and exit
 ```
 */5 * * * * python3 /home/[path]/run.py
 ```
 # Machine Learning Model for time series forecasting
 For the prediction model you can go for Jupyter notebook editor, you can find the file in time series forecasting folder. The dataset is available in the name of out.csv in same folder.
  - Top 20 place with lowest bike flow[mean]
  - Top 20 place with highest bike flow[mean]
  - Resampling the data
  - Finding Insights of data
     - Line plot
     - Trend, seasonal , Resid
  - Statistics
    - P -value
    - Autocorrelation
    - Partial Correlation
  - Forescasting the data
    - Autoregressive Integrated Moving Average (ARIMA) Model
    - Holt-Winters
  - Error rate

# Future Roadmap

If the data volume is high means we can get high accuracy , whilst we can go for the recurrent neural network (Deep Learning). Also we can add live weather data to get much more accuracy and hidden insights from the bike counts , But it will more time and need more volume of data.   
  
 
 
 
 
 
 
 
 
 
