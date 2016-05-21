largest = None
smallest = None
while True:
	num= raw_input("Enter a number: ")
	if num == "done":
		break	
	try:
		number = float(num)
		if smallest is None or number < smallest:
			smallest = number
		elif largest is None or number > largest:
			largest = number
	except:
		print 'invalid input'
	
print 'Maximum:', largest
print 'Minimum:' , smallest


	