import json
import urllib
serviceurl = " http://maps.googleapis.com/maps/api/geocode/json?"

while True:
	specify_location = raw_input("Enter Location : " )
	if len(specify_location)<1 : break
	
	url_extract= serviceurl + urllib.urlencode({'sensor':'false', 'address' :specify_location})
	print "Retreiving",url_extract
	uh = urllib.urlopen(url_extract)
	data = uh.read()
	print "Retrieved" , len(data), "Characters"
	
	try: info = json.loads(str(data))
	except: info = None
	if 'status' not in info or info['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		print data
		continue

	place_id = info["results"][0]["place_id"]
	print "Place ID:",place_id
	break
	
	
