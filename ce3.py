def computepay(h,r):
    
    if hours <= 40:
        reg_pay = hours * rate
        print reg_pay
	else
        ot = hours - 40
    	ot_rate = rate * 1.5
    	ot_pay = (ot * ot_rate) + ( 40 * rate)
    return ot_pay

hrs = raw_input("Enter Hours:")
rt = raw_input ("Enter Rate:")
hours = float(hrs)
rate = float (rt)

print computepay(h,r)

p = computepay(10,20)
print p