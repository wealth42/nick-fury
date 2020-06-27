import sys
import MySQLdb
import secret

#This file supposed to be run separately

def connection():
	con = MySQLdb.connect(host=secret.host,
							user=secret.user,
							passwd=secret.password,
							db=secret.db1)
	cur = con.cursor()
	return con,cur

def strip(s):
	return s.strip().lower()

def check(commonName,cur):
	query = """SELECT terminal_info.TerminalName,terminal_info.nbBike,terminal_info.nbEmptyDock,terminal_info.nbDock,terminal_info.datet FROM terminal_info,terminal WHERE CommonName=%s and terminal.TerminalName=terminal_info.TerminalName;"""
	cur.execute(query,(commonName,))
	ans = cur.fetchall()[0]

	print("Terminal name :",ans[0])
	print("No. of bikes available :",ans[1])
	print("No. of empty docs :",ans[2])
	print("No. of total docks :",ans[3])
	print("Datetime :",ans[4])	


if __name__ == "__main__":	
	con,cur=connection()
	argument = " ".join(sys.argv[1:])
	commonName = " ".join(list(map(strip,argument.split(','))))
	check(commonName,cur)


