import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
count=0

ite = int(7)
#position = raw_input('Enter the position-')
#pos = int(count)
while ite > 0:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags :
		url = tag.get('href', None)
    	count=count+1
    	if count == 18:
    		print url
    	
    	
    	#copy=url
    	#html = urllib.urlopen(copy).read()
#soup = BeautifulSoup(html)
#another_tags = soup('a')
#for another_tag in another_tags:
	#content = another_tag.contents[0]
	#print content
    	