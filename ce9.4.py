dict = {}
bigcount = None
bigword = None
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
	line = line.strip()
	if not line.startswith('From '): continue
	words = line.split()
	mail= words [1]
	dict[mail] = dict.get(mail,0)+1
for key , value in dict.items():
	if bigcount is None or value > bigcount:
		bigcount= value
		bigword = key
print bigword, bigcount	
	
	
	
	