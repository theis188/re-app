import random
import readcoords
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import urllib2

def get_random_point_in_polygon(poly):
     (minx, miny, maxx, maxy) = poly.bounds
     while True:
         p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
         if poly.contains(p):
             return p

def get_walkscore(coord):


coords = readcoords.coords()

xy = coords[coords.keys()[0]]
xylist = zip(*xy)

p = Polygon(xylist)

points = [get_random_point_in_polygon(p) for i in range(100)]

ax = plt.subplot()
ax.plot(*xy)
for point in points: ax.plot(point.x,point.y,marker = 'o')

plt.show()