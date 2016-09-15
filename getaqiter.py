import urllib2
import re

Areas = ['Central LA Co','NW Coastal LA','SW Coastal LA','S Coastal LA','Southeast LA Co','W San Fernando Vly','E San Fernando Vly','W San Gabriel Vly','E San Gabriel Vly-1','E San Gabriel Vly-2','Pomona Walnut Vly','S San Gabriel Vly','S Central LA Co','Santa Clarita Vly','San Gabriel Mts','Antelope Vly']

website = urllib2.urlopen(r'http://www.aqmd.gov/home/library/air-quality-data-studies/daily-air-quality-forecast')

