
def main():
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
  
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = ' X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
			
def match_ends(words):
	count=0
	for i in words:
		if i[0] == i[-1] and len(i)>=2:
			count = count+ 1
	return count


		
	