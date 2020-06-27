from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Layout_table import Base,table_structure
import os
#connect to database
def database_connect():
    path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(os.getenv('User_name'),os.getenv('Password'),os.getenv('Port'),os.getenv('Db_name'))
    engine = create_engine(path)  
    return engine


#create a session
def Session_create(sess_engine):
	sess_maker = sessionmaker()
	sess_maker.configure(bind=sess_engine)
	sess = sess_maker()
	return sess

#Fetch the data from database
    
def fetch(sess,locate):
    list_data = locate.split()
    final_str = str()
    for i in range(len(list_data)):
        list_data[i] =list_data[i].capitalize()
        final_str+=list_data[i]+' '
    final_str+='%'
    result = sess.query(table_structure).filter(table_structure.name_of_loaction.like(final_str)).all()
    return result[0].__dict__

#get user Inputs

def get_input_From_user():
    city = input("Enter The name of the City or Loacation :  ")
    return city

#display of final Results
def display(final_res):
        print("------------------------------------" )
        print(" Bike Id  {} \n Common Name {} \n Available Bikes {} \n Empty Docks {} \n Total Docks {} \n Date & Time of upadate   {}".format(final_res['bike_id'],final_res['name_of_loaction'],final_res['available_bikes'],final_res['empty_docks'],final_res['total_docks'],str(final_res['date_of_update'])+' '+str(final_res['time_of_update'])))

if __name__=="__main__":
    eng = database_connect()
    sess = Session_create(eng)
    inp  = get_input_From_user()
    res = fetch(sess,inp)
    display(res)

    
    
