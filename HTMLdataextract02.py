import urllib
from BeautifulSoup import *
count=0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
   	url_one= tag.get('href', None)
   	count=count+1
   	if count==18:
   		print url_one
		url_two = url_one
		html= urllib.urlopen(url_two).read()
soup = BeautifulSoup(html)
tags_two = soup('a')
count_two=0
for tag_two in tags_two:
   	url_three= tag_two.get('href', None)
   	count_two=count_two+1
   	if count_two==18:
   		print url_two
		url_two = url_three
		html= urllib.urlopen(url_three).read()
soup = BeautifulSoup(html)
tags_three = soup('a')
count_three=0
for tag_three in tags_three:
   	url_three= tag_three.get('href', None)
   	count_three=count_three+1
   	if count_three==18:
   		print url_three
		url_four = url_three
		html= urllib.urlopen(url_four).read()
soup = BeautifulSoup(html)
tags_four = soup('a')
count_four=0
for tag_four in tags_four:
   	url_four= tag_four.get('href', None)
   	count_four=count_four+1
   	if count_four==18:
   		print url_four
		url_five = url_four
		html= urllib.urlopen(url_five).read()
soup = BeautifulSoup(html)
tags_five = soup('a')
count_five=0
for tag_five in tags_five:
   	url_five= tag_five.get('href', None)
   	count_five=count_five+1
   	if count_five==18:
   		print url_five
		url_six = url_five
		html= urllib.urlopen(url_six).read()
soup = BeautifulSoup(html)
tags_six = soup('a')
count_six=0
for tag_six in tags_six:
   	url_six= tag_six.get('href', None)
   	count_six=count_six+1
   	if count_six==18:
   		print url_six
		url_seven = url_six
		html= urllib.urlopen(url_seven).read()
soup = BeautifulSoup(html)
tags_seven = soup('a')
count_seven=0
for tag_seven in tags_seven:
   	url_seven= tag_seven.get('href', None)
   	count_seven=count_seven+1
   	if count_seven==18:
   		print url_seven
#  		url_eight = url_seven
#		html= urllib.urlopen(url_eight).read()
#soup = BeautifulSoup(html)
#tags_eight = soup('a')
#for tag_eight in tags_eight:
 #  	url_eight= tag_eight.get('href', None)
  # 	print url_eight###
   