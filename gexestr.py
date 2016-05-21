def donuts(count):
        if count >10:
        	return 'Number of Donuts:many'
        else:
        	return 'Number of Donuts:' + str(count)
print donuts(4)        	
print donuts(9) 
print donuts(10)
print donuts(99)