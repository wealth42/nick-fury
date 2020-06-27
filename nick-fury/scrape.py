import json
import requests
import datetime
import MySQLdb
import time

def strip(s):
	return s.strip().lower()

def task(con1,cur1,con2,cur2):
	print("Task started")

	start =  time.time()
	url = "https://api.tfl.gov.uk/bikepoint"
	response = requests.get(url)
	data = response.text
	data = json.loads(data)

	for i in range(len(data)):
		try:
			terminal = {}
			terminal['id']=data[i]['id']
			terminal['commonName']=" ".join(list(map(strip,data[i]['commonName'].split(','))))
			
			info = {}
			for j in data[i]['additionalProperties']:
				if(j['key']=='TerminalName'):
					terminal['terminalName']=j['value']
					info['terminalName']=j['value']
				elif(j['key']=='NbBikes'):
					info['nbBike']=j['value']
				elif(j['key']=='NbEmptyDocks'):
					info['nbEmptyDock']=j['value']
				elif(j['key']=='NbDocks'):
					info['nbDock']=j['value']

			for j in range(len(data[i]['additionalProperties'])):
				if("modified" in data[i]['additionalProperties'][j]):
					d=data[i]['additionalProperties'][j]['modified'].split('T')
					break

			date = list(map(int,d[0].split("-")))
			Time = d[1].split('.')[0].split(':')
			if('Z' in Time[2]):
				Time[2]=Time[2][:Time[2].index('Z')]
			Time = list(map(int,Time))

			dateTime = datetime.datetime(date[0],date[1],date[2],Time[0],Time[1],Time[2])
			info['datetime']=dateTime


			query = """INSERT INTO terminal_info(TerminalName,nbBike,nbEmptyDock,nbDock,datet) VALUES(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE \
					TerminalName=VALUES(TerminalName),\
					nbBike=VALUES(nbBike),\
					nbEmptyDock=VALUES(nbEmptyDock),\
					nbDock=VALUES(nbDock),\
					datet=VALUES(datet);"""

			tup = (info['terminalName'],info['nbBike'],info['nbEmptyDock'],info['nbDock'],info['datetime'])
			cur1.execute(query,tup)
			con1.commit()

			query = """INSERT IGNORE INTO terminal_info(TerminalName,nbBike,nbEmptyDock,nbDock,datet) VALUES(%s,%s,%s,%s,%s);"""
			cur2.execute(query,tup)
			con2.commit()
		
			query = """INSERT IGNORE INTO terminal(Terminal_id,CommonName,TerminalName) VALUES(%s,%s,%s);"""
			cur1.execute(query,(terminal['id'],terminal['commonName'],terminal['terminalName'],))
			con1.commit()

			cur2.execute(query,(terminal['id'],terminal['commonName'],terminal['terminalName'],))
			con2.commit()			
		except Exception as e:
			print(e)
			break

	print("Excution time :",time.time()-start)
	print("DONE")
	print()

url = "https://api.tfl.gov.uk/bikepoint"
response = requests.get(url)
data = response.text
data = json.loads(data)

