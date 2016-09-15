import urllib2
import re
import ast
import matplotlib.pyplot as plt

ham = urllib2.urlopen(r"http://maps.latimes.com/neighborhoods/neighborhood/angeles-crest/")
listneighbs=[]
goodname=[]

for lines in ham:
	f = re.search(r'<option value="(.+)">(.+)</option>',lines)
	if f: 
		listneighbs.append(f.group(1))
		goodname.append(f.group(2))
		if 'woodland-hills' in listneighbs: break


thisfile=open('neighburls.txt','w')
for lines in listneighbs:
	thisfile.write(lines + "\n")

thisfile=open('neighbnames.txt','w')
for lines in goodname:
	thisfile.write(lines + "\n")
