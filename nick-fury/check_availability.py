import sys
import MySQLdb


con1 = MySQLdb.connect(host='localhost',
							user='root',
							passwd="ankit@02217",
							db='realtimebikepoint')
cur1 = con1.cursor()


def strip(s):
	return s.strip().lower()

argument = " ".join(sys.argv[1:])
commonName = " ".join(list(map(strip,argument.split(','))))


query = """SELECT terminal_info.TerminalName,terminal_info.nbBike,terminal_info.nbEmptyDock,terminal_info.nbDock,terminal_info.datet FROM terminal_info,terminal WHERE CommonName=%s and terminal.TerminalName=terminal_info.TerminalName;"""
cur1.execute(query,(commonName,))
ans = cur1.fetchall()[0]

print("Terminal name :",ans[0])
print("No. of bikes available :",ans[1])
print("No. of empty docs :",ans[2])
print("No. of total docks :",ans[3])
print("Datetime :",ans[4])