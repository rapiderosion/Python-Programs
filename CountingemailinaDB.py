import sqlite3

conn=sqlite3.connect('emaildb.sqlit')
cur = conn.cursor()

cur.execute ('''
DROP TABLE IF EXISTS Counts''')

cur.execute ('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fhand= raw_input("Enter a filename-:")
if (len (fhand)<1): fhand= 'mbox.txt'
fh = open(fhand)
for line in fh:
	if not line.startswith('From'): continue
	split = line.split()
	email = split[1]
	cur.execute ('SELECT count FROM Counts WHERE email =?',(email, ))
	try:
		count = cur.fetchone ()[0]
		cur.execute ('Update Counts SET count=count+1 WHERE email = ?', (email,))
	except:
		cur.execute ('''INSERT INTO Counts (email, count)
			VALUES (?,1)''', (email,))
	conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
	print str(row[0]),row[1]

cur.close