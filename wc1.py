f= open ('/Users/guest/Desktop/small.txt', 'r')
word_count = {}
for wordy in f:
	words = wordy.split()
	for wor in words :
		word = wor.lower()
		if not word in wor:
			word_count[word] = 1
			print word_count[word], word
		else:
			word_count[word] = word_count[word]+1
			print word_count

		
		
			
			
			