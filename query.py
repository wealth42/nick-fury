import mysql.connector

def script(s):
    try:
        db = mysql.connector.connect(user='', password='',#user & #password
                                     host='127.0.0.1', database="bikepoint")
        cursor = db.cursor()
        querry='SELECT * FROM bikepoint.point where commonName like \'%{query}%\';'
        cursor.execute(querry.format(query=s))
        result=cursor.fetchall()
        for res in result:
            print(res[8],'bikes',"\tAvailable at",res[2])
        print('Found Locations: ',len(result))
        db.close()
    except mysql.connector.Error as err:
        print('found error', err)

if __name__ == '__main__':
    print("Type to search no. of bikes available")
    query=input('Enter a location :\t')
    script(query)
