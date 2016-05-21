import urllib
import xml.etree.ElementTree as ET
total=0
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')
    print 'Number Count' , len (results)
    for items in results:
    	numbers= int(items.find ('count').text)
    	total=total+numbers
    print total
    	

