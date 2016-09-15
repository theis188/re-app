import urllib2
import re

listurls = open('neighburls.txt','r')
basurl = r"http://maps.latimes.com/neighborhoods/neighborhood/"
for name in listurls:
	fullurl = basurl+name.rstrip()+r'/'
	print fullurl
	webpage = urllib2.urlopen(fullurl)
	for lines in webpage:
		d = re.search(r"geometry.+(\[ \[ \[ \[.+\] \] \] \])",lines)
		if d:
			coordlist = d.group(1)
			coordfile = open(r'Coords/' + name.rstrip() + '.txt','w')
			coordfile.write(coordlist)