import requests
import mysql.connector
import json
import threading


def script():
    try:
        #connecting database
        result = requests.get('https://api.tfl.gov.uk/bikepoint')
        db = mysql.connector.connect(user='', password='',#user & #password
                                     host='127.0.0.1', database="bikepoint")
        cursor = db.cursor()
        
        sql_point = "replace into point values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql_addons = "replace into addons values ( %s, %s, %s, %s, %s, %s)"

        for point_data in result.json():
            final_point_data = point_data
            for key in point_data:
                if type(point_data[key]) != str:
                    final_point_data[key] = json.dumps(final_point_data[key])

            additional_properties = (final_point_data.pop('additionalProperties')[1:-2].split('}, '))
            
            final_point_data.pop('$type')
            for addon in additional_properties:
                final_addon_data = dict()
                final_addon_data['id'] = final_point_data['id']
                data = json.loads(addon + '}')
                for key in data:
                    final_addon_data[key] = data[key]

                final_addon_data.pop('$type')
                if data['key'] == 'NbDocks': final_point_data['docks'] = data['value']
                if data['key'] == 'NbBikes': final_point_data['bikes'] = data['value']
                if data['key'] == 'NbEmptyDocks': final_point_data['spaces'] = data['value']
                val_addon = tuple(final_addon_data.values())
                cursor.execute(sql_addons, val_addon)

            val_point = tuple(final_point_data.values())
            cursor.execute(sql_point, val_point)
        db.commit()
        print(cursor.rowcount, "record inserted.")
        db.close()

    except mysql.connector.Error as err:
        print('found error', err)


def looper():
    global elapsed
    threading.Timer(300.0, looper).start()
    print("Time Passed : ", elapsed, "minutes")
    elapsed += 5
    script()


if __name__ == '__main__':
    elapsed = 0
    looper()
