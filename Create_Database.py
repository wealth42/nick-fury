from sqlalchemy_utils.functions import create_database,database_exists
import os

path = 'mysql+mysqlconnector://{}:{}@localhost:{}/{}'.format(os.getenv('User_name'),os.getenv('Password'),os.getenv('Port'),os.getenv('Db_name'))


#create Database .......
def create_database_in_msql():
    try:
       if database_exists(path):
           print('Database Already Exist Need not to create New One')
       else:
            create_database(path)
    except Exception as e:
      print(e)
      
if __name__ == '__main__':
    create_database_in_msql()
