def not_bad (s): 
	
	
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
  
def main():
  print 'not_bad'
test(not_bad('This movie is not so bad'), 'This movie is good')
test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
test(not_bad('This tea is not hot'), 'This tea is not hot')
test(not_bad("It's bad yet not"), "It's bad yet not")