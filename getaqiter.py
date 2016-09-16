import urllib2
import re
import os 
import sys
import time

basepath = r"C:\Users\Matt\Desktop\Python_App\RE_App\Data\AQI"
Areas = ['Central LA Co','NW Coastal LA','SW Coastal LA','S Coastal LA','Southeast LA Co','W San Fernando Vly','E San Fernando Vly','W San Gabriel Vly','E San Gabriel Vly-1','E San Gabriel Vly-2','Pomona Walnut Vly','S San Gabriel Vly','S Central LA Co','Santa Clarita Vly','San Gabriel Mts','Antelope Vly']

# if not ('aqi.csv' in os.listdir(basepath)):
# 	file = open(basepath + r'\aqi.csv','w')
# 	for area in Areas:
# 		file.write(area+', \n')
# 	sys.exit()


website = urllib2.urlopen(r'http://www3.aqmd.gov/smog/data/forecast.txt')
mmddyyyy = time.strftime(r"%m%d%Y")
file = open(basepath + r'\aqi'+mmddyyyy+'.csv','w')

for area in Areas:
	for line in website:
		if re.search(area,line):
			digs = re.search(r'(\d*\.*\d+) +(\d*\.*\d+) +(\d*\.*\d+) +(\d*\.*\d+) +(\d*\.*\d+) +(\d*\.*\d+) +(\d*\.*\d+)',line)
			vals = [ digs.group(i) for i in [1,2,3,4,5,6,7] ]
			file.write(area + ',' + ', '.join(vals) + '\n' )
			break