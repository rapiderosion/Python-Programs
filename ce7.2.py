count=0
total = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
    	pure_line = line.strip()
    	fin_zero = pure_line.find("0")
    	extract_num = pure_line [20:]
    	flo_num = float(extract_num)
    	total = flo_num + total
    	count+=1
ave = total/count
print "The total of the number is",total
print "The simple average of the numbers is" ,ave

