import urllib2
import re

savefile = open(r'Data\propcrim.txt','w')
output = [];
a=0
waitfor=0
website = urllib2.urlopen(r"http://maps.latimes.com/neighborhoods/property-crime/neighborhood/list/")

for line in website:
	
	d = re.search(r'<a name=".+" href="/neighborhoods/neighborhood/(.+)/crime/">(.+)</a>',line)
	if d:	
		neighbname = [d.group(1), d.group(2)]
			
	if waitfor: 
		c = re.search(r'(\d+,*\.*\d*)', line)
		if c:
			output.append(c.group(1))
			waitfor = 0

	e = re.search(r'<td width="15%"  style="font-size:17px; padding-left:5px; line-height:160%; text-align:right;">', line)
	if e: 
		waitfor=1
	
	if len(output) == 2:
		savefile.write(neighbname[0] + ', ' + neighbname[1] + ', ' + output[0] + ', ' + output[1] + '\n')
		output = []