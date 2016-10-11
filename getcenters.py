import os
import ast
from shapely.geometry import Polygon, Point
from getscores import getrank
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np

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

def mean(arr):
	return sum([float(i) for i in arr])/float(len(arr))

avcols = ['viol-crime','school-qual','prop-crime','air-qual']
# avcols = ["pop-dens-h","rest-dens","prop-crime"]
pricecol = ['buy-price']

avscores = {name: float(scorey) for (name,scorey) in zip(goodnames,getrank(avcols))}
pscores = {name: float(scorey) for (name,scorey) in zip(goodnames,getrank(pricecol))}
# print findnearest('central-alameda',5)
# ne = 'central-alameda'
# print 'overall score',avscores[ne]
# print 'price score',pscores[ne]
# print 'nearest 5',findnearest(ne,5)
# print 'nearest 5 overall scores',[ avscores[name] for name in findnearest(ne,5) ]
# print 'nearest 5 price scores',[ avscores[name] for name in findnearest(ne,5) ]
#print pscores
diffav = {}
diffp = {}
for ne in goodnames:
	narray = findnearest(ne,10)
	neavsc = float(avscores[ne])
	nepsc = float(pscores[ne])
	nearavsc = mean( [ avscores[name] for name in narray ] )
	nearpsc = mean( [ pscores[name] for name in narray ] )
	diffav[ne] = neavsc-nearavsc
	diffp[ne] = nepsc-nearpsc
	# print ne,neavsc,'rank score vs',nearavsc,'for nearby'
	# print ne,nepsc,'price score vs',nearpsc,'for nearby'

	# aaa = raw_input('aaa')

def onpick3(event):
	ind = event.ind
	print 'neighborhood:', goodnames[ind]


x=diffav.values()
y=diffp.values()

# x=[avscores[name] for name in goodnames]
# y=[pscores[name] for name in goodnames]

xx = np.array(x).reshape( (155,1) )
yy = np.array(y).reshape( (155,1) )

print xx.shape
print yy.shape

regr = linear_model.LinearRegression()
regr.fit(xx,yy)
print regr.score(xx,yy)

fig = plt.figure()
ax = fig.add_subplot(111)
col = ax.scatter(x, y, picker=True)
plt.xlabel('Other-Rank Difference (neighborhood-nearby)')
plt.ylabel('Price-Rank Difference (neighborhood-nearby)')
fig.canvas.mpl_connect('pick_event', onpick3)
plt.show()



x=avscores.values()
y=pscores.values()

ax = plt.subplot()
ax.plot(x,y,linestyle='None',marker='o')
plt.xlabel('Other-Rank')
plt.ylabel('Price-Rank')
plt.show()