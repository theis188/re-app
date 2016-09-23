import readcoords
import shapely
import genpoints
from shapely.geometry import Polygon, Point
from callyelp import restnumber

randpoint = genpoints.get_random_point_in_polygon

file = open('goodnames.txt')
namelist = [name.strip() for name in file]

coordlist = readcoords.coords(namelist)

num2get = 1

startnum = len(list(open(r'Data/restaurants.csv')))

r='350'

myfile = open(r'Data/restaurants.csv', "a")

for i in range(startnum,startnum+num2get):
	key = coordlist.keys()[i]
	print key
	xy = coordlist[key]
	xylist = zip(*xy)
	poly = Polygon(xylist)
	restNumList = []
	for j in range(50):
		pt = randpoint(poly)
		num = restnumber(str(pt[0]),str(pt[1]),r)
		print num
		restNumList.append(num)
	towrite = key + ',' + ','.join(str(i) for i in restNumList) + ',' + r
	print towrite
	aaa = raw_input('confirm?')
	myfile.write(towrite+'\n')
	
print 'exiting...'