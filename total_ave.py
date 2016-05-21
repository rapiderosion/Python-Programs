total = 0
count = 0
while True:
	num = raw_input("Enter a number>: ")
	if num == "done":
		break	
	try:
		number = float(num)
		total = number + total
		count = count + 1
		ave = total/count
		
	except:
		print "invalid input"

print " There are %s numbers" % count
print " Sum total of %s numbers is %s:" % (count,total)
print " Average of %s numbers is %s:" % (count, ave )