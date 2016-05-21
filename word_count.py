#declarations
dict = {}
bigcount = None
bigword= None
#opening a file
fname = raw_input ("Enter a Filename: ")
fh = open (fname , 'r')
# tearing open a file to get words and their count
for line in fh:
	line = line.lower()
	line = line.split()
	for word in line:
		dict[word] = dict.get(word,0) + 1
#finding out the word used the maximum number of times
for key , value in sorted(dict.items()):
	if bigcount is None or value > bigcount:
		bigcount = value
		bigword = key
print bigword, "->", bigcount
		
	

			