grade = raw_input("Enter a Grade:")
gr = float(grade)
if gr >=1.0 and grade <= 0.0:
	print "Out of Range"
elif gr >= 0.9:
  	print "A"
elif gr >= 0.8:
    print "B"
elif gr >=0.7:
    print "C"
elif gr >= 0.6:
    print "D"

else:
    print"F"