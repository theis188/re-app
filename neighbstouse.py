import urllib2
import re

urls = ['http://maps.latimes.com/neighborhoods/region/san-fernando-valley/',
'http://maps.latimes.com/neighborhoods/region/verdugos/',
'http://maps.latimes.com/neighborhoods/region/santa-monica-mountains/',
'http://maps.latimes.com/neighborhoods/region/northeast-la/',
'http://maps.latimes.com/neighborhoods/region/eastside/',
'http://maps.latimes.com/neighborhoods/region/central-la/',
'http://maps.latimes.com/neighborhoods/region/south-la/',
'http://maps.latimes.com/neighborhoods/region/south-bay/',
'http://maps.latimes.com/neighborhoods/region/westside/'
]

neighbnames = []

for website in urls:
	site = urllib2.urlopen(website)
	for line in site:
		item = re.search('slug: "(.+)",',line)
		if item:
			neighbnames.append(item.group(1))


print neighbnames

file = open('goodnames.txt','w')
for name in neighbnames:
	file.write(name+'\n')