from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json
import urllib2
import requests

def restnumber(x,y,r):
	with io.open('config_secret.json') as cred:
	    creds = json.load(cred)
	    auth = Oauth1Authenticator(**creds)
	    client = Client(auth)

	params = {
	    'term': 'restaurant',
	    'lang': 'en',
	    'limit': '20',
	    'radius_filter': r,
	    'cll': y+','+x
	    }

	API_KEY = open('gapi.txt').next()

	gurl = 'https://maps.googleapis.com/maps/api/geocode/json'
	gparams = {'sensor': 'false', 'latlng': y+','+x ,'key': API_KEY}
	#print gparams
	
	r = requests.get(gurl, params=gparams)
	results = r.json()['results']
	addy = results[0]['formatted_address']
	

	result =  client.search(addy, **params)#.businesses[1].location.coordinate.latitude
	return len(result.businesses)