from sqlalchemy import create_engine
from sqlalchemy.sql import text
from mysql_details import *
import pandas as pd

#Fetch Data from Database
def get_data(place):
    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}/bikepoints".format(Username, Password, Host))
        query=text("SELECT Name,TotalDocks,AvailableBikes,EmptyDocks FROM `bikepoints data` where Name Like '%{}%';".format(place))
        df = pd.read_sql_query(query,engine)
        return df
    except Exception as e:
        print(e)


#search query and display all the matching records
def search():
    while True:
        place=input("Enter place: ")
        details=get_data(place.strip())
        for i in list(details.index):
            a,b,c,d=details.iloc[i,:]
            print("""\n{}\nAvailable Bikes: {}\nEmpty Docks: {}\nTotal Docks: {}\n""".format(a,c,d,b))

        if "no" in input("Do you want to search more(yes/no): \n").lower():
            break



if __name__=="__main__":
    search()
