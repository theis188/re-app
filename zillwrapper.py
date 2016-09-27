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
	addlist = results[0]['address_components']
	ZIP = getaddprop(addlist,'postal_code')
	sn = getaddprop(addlist,'street_number')
	rt = getaddprop(addlist,'route')

	#print results
	WAIT = raw_input('WAIT')

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

	tree = ET.parse('xml.txt')
	
	amount = tree.find('response/results/result/zestimate/amount').text
	houseUrl = tree.find('response/results/result/links/homedetails').text
	#######if not

	return amount

randpoint = genpoints.get_random_point_in_polygon

file = open('goodnames.txt')
namelist = [name.strip() for name in file]
coordlist = readcoords.coords(namelist)

num2get = 1

openfile = open(r'Data/prices.csv', "r")
donelist = []

for line in openfile:
	donelist.append(line.split(',')[0])
openfile.close()
print donelist
aaa = raw_input('already done continue?')

myfile = open(r'Data/prices.csv', "a")
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
	while len(buyprices) < 1:
		pt = randpoint(poly)
		price = buyprice(str(pt[0]),str(pt[1]))
		buyprices.append(price)

	



