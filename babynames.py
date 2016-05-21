dict = {}
# opening a file
handle = open("1992.txt", 'r')
for lines in handle:
	if not lines.startswith ("<td>"): continue
	line=lines.split()
	print line

	