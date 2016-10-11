import os
import ast
from shapely.geometry import Polygon, Point

basepath = 'Coords/'
coordl = {}
centers = {}
goodnames = []

gopen = open('goodnames.txt','r')
for line in gopen:
	goodnames.append( line.strip() )

# cols=
# getdata(cols)

filelist = os.listdir(basepath)
for fname in filelist:
	name = fname.split('.')[0].strip()
	if not (name in goodnames):
		continue
	cfile = open(basepath+fname)
	line = cfile.next()
	coords = ast.literal_eval(line)
	lens = [len(i[0]) for i in coords]
	ind = [i for i,j in enumerate(lens) if j==max(lens)][0]
	xylist = coords[ind][0]
	coordl[name] = xylist

for name in coordl:
	p = Polygon(coordl[name])
	centers[name] = [p.centroid.x,p.centroid.y]

def dist(p1,p2):
	return ( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )**0.5

def findnearest(name,n):
	dists = [(dist(centers[name],centers[iname]),iname) for iname in centers]
	sort = sorted(dists)
	return [j[1] for i,j in enumerate(sort) if i in range(1,n+1)]

print findnearest('santa-monica',10)