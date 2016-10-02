# import urllib2
# import re

# baseurl = r'http://maps.latimes.com/neighborhoods/neighborhood/'
# file = open('goodnames.txt','r')
# densfile = open('Data/Final/pdf.csv','w')

# for line in file:
# 	print line.strip()
# 	web = urllib2.urlopen(baseurl+line.strip()+'/')
# 	for webline in web:
# 		dens = re.search(r'<li><strong>([\d,\.]+)</strong> people per square mile,',webline)
# 		if dens:
# 			densnum = dens.group(1)
# 			densnum = densnum.replace(',','')
# 			densfile.write(line.strip()+','+densnum+'\n')
# 			print line.strip()+','+densnum+'\n'

neighbs = []
file = open('goodnames.txt','r')
for line in file:
	neighbs.append(line.strip())
file.close()

ninfile = []
infile = open('Data/Final/pdf.csv','r')
for line in infile:
	ninfile.append(  line.split(',')[0].strip()  )

infile.close()

writefile = open('Data/Final/pdf.csv','a')
for n in neighbs:
	if (n not in ninfile):
		writefile.write(n+',\n')
		