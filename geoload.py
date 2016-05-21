import urllib
import json
import sqlite3
import time

serviceurl ="http://maps.googleapis.com/maps/api/geocode/json?"

conn= sqlite.connect ('geodata.sqlite')
cur = conn.cursor ()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations ( address TEXT ,geodata TEXT)''')

fh = open ("where.data")
count = 0
for line in fh:
	if count >200 : break
	address = line.strip()
	print ''
	cur.execute ( '''SELECT geodata FROM Locations WHERE address = ?''', (buffer(address),))
	
	try:
		data = cur.fetchone()[0]
		print "Found in DB", address
		continue
	except:
		pass
	print "Resolving", address
	url= serviceurl+urllib.urlencode ({"sensor":"false", "address": address})
	print "Retrieving", url
	uh = urllib.urlopen (url)
	data = uh.read()
	print 'Retrieved' , len(data), 'characters', data [:20]. replace ('\n','')
	

