import schedule
import time
import scrape
import datetime
import MySQLdb
import getpass
import secret

try:
	con1 = MySQLdb.connect(host=secret.host,
							user=secret.user,
							passwd=secret.password,
							db=secret.db1)
	cur1 = con1.cursor()

	con2 = MySQLdb.connect(host=secret.host,
							user=secret.user,
							passwd=secret.password,
							db=secret.db2)

	cur2 = con2.cursor()
	print("======Connection Established======")
except Exception as e:
	print("======Connection Failed======")
	print("Error :",e)
	pass


scrape.task(con1,cur1,con2,cur2)

schedule.every(5).minutes.do(scrape.task,con1,cur1,con2,cur2)
while 1:
	schedule.run_pending()
	time.sleep(1)