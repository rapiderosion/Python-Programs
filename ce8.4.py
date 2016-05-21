fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.lower()
	line1 = line.split()
	for word in line1:
		if not word in lst:
			lst.append(word)
			count = 1						
		else:
			count = count+1
			print word, count
		
			

		


			
			
			
			
	
	