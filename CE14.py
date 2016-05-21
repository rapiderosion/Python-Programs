import re
total= 0
count = 0
fhand = open ('regex_sum.txt') 
for line in fhand:
	numb = re.findall('[0-9]+', line)
	if len(numb) > 0:
		for indi in numb:
			total= int(indi)+total
			count=count+1
print total, count
			
	
	
	
	
	
