import sqlite3

conn= sqlite3.connect ('emaildb.sqlite')
cur=conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
fname = raw_input ("Enter File Name: ")
if (len(fname)<1): fname= 'mbox.txt'
fh= open(fname)
for line in fh:
	if not line.startswith ('From'): continue
	pieces = line.split()
	email = pieces[1]
	print email