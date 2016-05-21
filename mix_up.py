def mix_up (a,b):
	if (len (a) and len (b)) > 2:
		a_swapped = a[:2] + b[2:]
		b_swapped = b[:2] + a[2:]
		return  a_swapped +" " + b_swapped
	else:
		print " word has to be more than two letters. This selection is ignored"
def main ():
    print mix_up('mix', 'pod')
    print mix_up('dog', 'dinner')
    print mix_up('gnash', 'sport')
    print mix_up('pezzy', 'firm')
    print mix_up('ab', 'cd')

print main()