import json
import urllib
serviceurl = "http://python-data.dr-chuck.net/comments_187014.json?"
total=0
while True:
	specify_location = raw_input("Enter Location : " )
	if len(specify_location)<1 : break
	url_extract= serviceurl + urllib.urlencode({'sensor':'false', 'address' :specify_location})
	print "Retreiving",url_extract
	uh = urllib.urlopen(url_extract)
	data = uh.read()
	print "Retrieved" , len(data), "Characters"
	info = json.loads(str(data))
	for x in info["comments"]:
		number = x['count']
		total = total+number
	print "Sum of the numbers in the JSON extract is", total
	break

		
	
	
	
	
	
