import xml.etree.ElementTree as ET
import io
import json
import urllib2
import requests
import shapely
import genpoints
from shapely.geometry import Polygon, Point
from callyelp import restnumber
import urllib2
import re
import time
import readcoords

def getaddprop(alist,comp):
	clist = [i for i in alist if comp in i['types']]
	return clist[0]['long_name']

def buyprice(x,y):    
	API_KEY = open('gapi.txt').next()

	gurl = 'https://maps.googleapis.com/maps/api/geocode/json'
	gparams = {'sensor': 'false', 'latlng': y+','+x ,'key': API_KEY}
	#print gparams
	
	r = requests.get(gurl, params=gparams)
	results = r.json()['results']
	try:
		addy = results[0]['formatted_address']
		print addy
	except:
		return "except"
	try:
		addlist = results[0]['address_components']
		ZIP = getaddprop(addlist,'postal_code')
		sn = getaddprop(addlist,'street_number')
		if re.search(r'-', sn): return 'except'
		rt = getaddprop(addlist,'route')
	except:
		print 'no address...'
		return "except"

	#print results

	zURL = r'http://www.zillow.com/webservice/GetSearchResults.htm'
	zKEY = open('zapi.txt').next()
	zparams = {
    'zws-id': zKEY,
    'address': sn+' '+rt,
    'citystatezip': ZIP,
    }

	zresult = requests.get(zURL, params=zparams)

	XMLstr = ''.join(zresult)

	xmlsamp = open('xml.txt','w')
	xmlsamp.write(XMLstr)
	xmlsamp.close()

	tree = ET.parse('xml.txt')
	
	amount = tree.find('response/results/result/zestimate/amount')
	houseUrl = tree.find('response/results/result/links/homedetails')

	if (amount is None) or (houseUrl is None):
		print 'bad address, no information returned'
		return 'except'

	amount = amount.text
	houseUrl = houseUrl.text
	schoollist = []
	beds = 0
	housepage = urllib2.urlopen(houseUrl)
	for line in housepage:
		bedsearch = re.search(r'<meta property="zillow_fb:beds" content="(\d+)">', line)
		if bedsearch:
			beds = bedsearch.group(1)
		schoolsearch = re.search(r'<span class="gs-rating-number gs-rating-(\d+)"', line)
		if schoolsearch:
			schoollist.append( int(schoolsearch.group(1)) )

	if int(beds) > 5:
		print 'too many beds:', beds
		return 'except'
	return [amount, sum(schoollist)/len(schoollist) ]

randpoint = genpoints.get_random_point_in_polygon

file = open('goodnames.txt')
namelist = [name.strip() for name in file]
coordlist = readcoords.coords(namelist)

num2get = 5

openfile = open(r'Data/prices.csv', "r")

donelist = []

for line in openfile:
	donelist.append(line.split(',')[0])
openfile.close()
print donelist
aaa = raw_input('already done continue?')

myfile = open(r'Data/prices.csv', "a")
schoolfile = open(r'Data/schools.csv', "a")
z=0
for i in range(len( coordlist.keys() )):
	if z == num2get: break
	key = coordlist.keys()[i]
	if key in donelist: continue
	z+=1
	print key
	xy = coordlist[key]
	xylist = zip(*xy)
	poly = Polygon(xylist)
	buyprices = []
	schools = []
	while len(buyprices) < 5:
		pt = randpoint(poly)
		ret = buyprice(str(pt[0]),str(pt[1]))
		if ret == 'except': continue
		price,school = ret
		if price == None: continue
		print 'success!'
		print 'price =', price
		print 'schoolq =', school
		buyprices.append(price)
		schools.append(school)
	towrite1 = key + ',' + ','.join(str(i) for i in buyprices)
	towrite2 = key + ',' + ','.join(str(i) for i in schools)
	print towrite1
	print towrite2
	aaa = raw_input('OK to write?')

	myfile.write(towrite1+'\n')
	schoolfile.write(towrite2+'\n')

print 'exiting...'
	



