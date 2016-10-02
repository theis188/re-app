import os
import matplotlib.pyplot as plt
import ast

def coords(nlist):

	#basepath = r"C:\Users\Matt\Desktop\Python_App\RE_App\Coords"
	basepath = r'Coords'

	#filelist = os.listdir(basepath)
	ax = plt.subplot()
	coordl = {}

	for file in nlist:
		lines = open(basepath + r'\\' + file+'.txt')
		for line in lines:
			coords = ast.literal_eval(line)
			lens = [len(i[0]) for i in coords]
			ind = [i for i,j in enumerate(lens) if j==max(lens)][0]
			xy = zip(*coords[ind][0])
			coordl[file] = xy

	return coordl

	print('Done!')
	for key in coordl.keys():
		ax.plot(*coordl[key])
			
	plt.show()