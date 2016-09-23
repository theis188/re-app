import readcoords
import shapely
import genpoints
from shapely.geometry import Polygon, Point
from callyelp import restnumber
import urllib2
import re
import time

randpoint = genpoints.get_random_point_in_polygon

file = open('goodnames.txt')
namelist = [name.strip() for name in file]

coordlist = readcoords.coords(namelist)

num2get = 1

openfile = open(r'Data/walkbiketrans.csv', "r")
donelist = []

for line in openfile:
	donelist.append(line.split(',')[0])
openfile.close()

print donelist
aaa = raw_input('already done continue?')

myfile = open(r'Data/walkbiketrans.csv', "a")

# coordfile = open('neighcoords.txt','w')
z = 0
for i in range(len( coordlist.keys() )):
	if z == num2get: break
	key = coordlist.keys()[i]
	if key in donelist: continue
	z+=1
	print key
	xy = coordlist[key]
	xylist = zip(*xy)
	poly = Polygon(xylist)
	bikescore = []
	walkscore = []
	transscore = []
	#coordfile.write(key+'\n')
	while max([len(bikescore),len(walkscore),len(transscore)])<12:
	#for j in range(10):
		pt = randpoint(poly)
		x = str(pt[0])
		y = str(pt[1])
		print y,x
		#coordfile.write(r'https://www.walkscore.com/score/loc/lat='+y+'/lng='+x+'\n')

		time.sleep(3)
		page = urllib2.urlopen(r'https://www.walkscore.com/score/loc/lat='+y+'/lng='+x)
		for line in page:
			score = re.search(r'<img src="//pp\.walk\.sc/badge/(.+)/score/(\d+)\.',line)
			if score:
				b = re.search(r'<img src="//pp\.walk\.sc/badge/bike/score/(\d+)\.',line)
				try:
					bikescore.append( int (b.group(1)) )
				except AttributeError:
					print 'bike error try again'
				w = re.search(r'<img src="//pp\.walk\.sc/badge/walk/score/(\d+)\.',line)
				try:
					walkscore.append( int (w.group(1)) )
				except AttributeError:
					print 'walk error try again'
				t = re.search(r'<img src="//pp\.walk\.sc/badge/transit/score/(\d+)\.',line)
				try:
					transscore.append( int (t.group(1)) )
				except AttributeError:
					print 'transit error try again'
	for i in [bikescore,walkscore,transscore]:
		if not i: i.append('NULL')
	towrite1 = key + ',bike,' + ','.join(str(i) for i in bikescore)
	towrite2 = key + ',walk,' + ','.join(str(i) for i in walkscore)
	towrite3 = key + ',transit,' + ','.join(str(i) for i in transscore)
	print towrite1
	print towrite2
	print towrite3
	aaa = raw_input('confirm?')
	myfile.write(towrite1+'\n')
	myfile.write(towrite2+'\n')
	myfile.write(towrite3+'\n')
	
print 'exiting...'

