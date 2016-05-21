import urllib
from BeautifulSoup import *
count=0
loop=0
while loop <7:
	url = raw_input('Enter - ')
	position = raw_input(" Enter the position -")
	pos= int(position)
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags:
   		url_one= tag.get('href', None)
   		count+=1
   		if count==pos:
   			print url_two
url_two=url_one