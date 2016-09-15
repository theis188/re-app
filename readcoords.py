import os
import matplotlib.pyplot as plt
import ast

basepath = r"C:\Users\Matt\Desktop\Python_App\RE_App\Coords"

filelist = os.listdir(basepath)
ax = plt.subplot()
coordl = {}

for file in filelist:
	lines = open(basepath + r'\\' + file)
	for line in lines:
		coords = ast.literal_eval(line)
		xy = zip(*coords[0][0])
		coordl[file] = xy

print('Done!')
for key in coordl.keys():
	ax.plot(*coordl[key])
		
plt.show()