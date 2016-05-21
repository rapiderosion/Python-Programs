dict = {}
t = list()
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
    #Splitting the file to extract the "From" line
for line in handle:
	line= line.strip()
	if not line.startswith ("From "): continue
	word= line.split()
	#Extracting the hour
	timesplit = word[5]
	timesplit = timesplit.split (":")
	time = timesplit[0]
	#counting the hours and passing into a dictionary
	dict[time] = dict.get(time,0) +1
	t = dict.items()
	#sorting the keys and printing 
for key , value in sorted(t):
	print key, value

	
	
	
		
		

		
	