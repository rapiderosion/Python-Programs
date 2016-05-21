def computepay(h,r):
    hours = float(hrs)
    rate = float (rt)
    if hours <= 40:
        reg_pay = hours * rate
        return reg_pay
    else:
       	ot_pay = ((hours - h)*(rate*1.5)) + (h * rate)
    return ot_pay

hrs = raw_input("Enter Hours:")
rt = raw_input ("Enter Rate:")
p = computepay(10,20)
print "Pay",p