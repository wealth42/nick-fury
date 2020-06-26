from sqlalchemy import create_engine
from mysql_details import *
import pandas as pd

#Fetch Data from Database
def get_data():
    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}/bikepoints".format(Username, Password, Host))
        df = pd.read_sql_table("bikepoints data", con=engine,columns=["Name", "Total Docks", "Available Bikes", "Empty Docks"])
        return df
    except Exception as e:
        print(e)


#search query and display all the matching records
def query(df):
    while True:
        place=input("Enter place: ")
        details=df.loc[df.Name.str.contains(place.strip(), case=False),:]
        for i in list(details.index):
            a,b,c,d=df.iloc[i,:]
            print("\n{}\nAvailable Bikes: {}\nEmpty Docks: {}\nTotal Docks: {}\n".format(a,c,d,b))

        if "no" in input("Do you want to search more(yes/no): \n").lower():
            break



if __name__=="__main__":
    query(get_data())