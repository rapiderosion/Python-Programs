def front_back(a,b):
	a_middle = len(a) / 2
	b_middle = len(b) / 2
	if len(a) %2 == 1:
		a_middle =+ 1
	if len(b) % 2 == 1:
		b_middle =+ 1
		return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]
	
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
  
def main():
  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')