import requests
import json

#credentials
api='https://api.tfl.gov.uk/bikepoint'
application_id='0165cf3a'
application_key='9187b8a0c05c716327bf753e55092b55'

#requesting for the details of the bike
resp=requests.get(api,auth=(application_id,application_key))

#looping through the response object
for each in resp.json():
	#details of bikestation and its availability
	bike_statn_name=each['commonName']
	status=each['additionalProperties'][2]['key']
	status_value=each['additionalProperties'][2]['value']

	if(status=="Locked" and status_value =="false" ):
		print('Bike is available at ',bike_statn_name)
	
	