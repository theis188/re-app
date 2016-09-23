import random
import readcoords
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import urllib2
from callyelp import restnumber

def get_random_point_in_polygon(poly):
     (minx, miny, maxx, maxy) = poly.bounds
     while True:
         p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
         if poly.contains(p):
             return [p.x,p.y]

#coords = readcoords.coords()

# xy = coords[coords.keys()[0]]
# xylist = zip(*xy)

# p = Polygon(xylist)

# points = [get_random_point_in_polygon(p) for i in range(5)]
# restaurants = [restnumber(str(point.x),str(point.y)) for point in points]

# print restaurants

# ax = plt.subplot()
# ax.plot(*xy)
# for point in points: ax.plot(point.x,point.y,marker = 'o')

# plt.show()