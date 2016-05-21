def both_ends(s):
	b_first = s[0:2]
	c_last = s[-2:]
  	if len(s) < 2:
  		return ' '
	else:
		return b_first + c_last
		
print both_ends("a")
print both_ends('spring')
print both_ends("Hello")
print both_ends("b")
print both_ends("xyz")

