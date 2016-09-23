
writefile = open('LA.js','w')
file1 = open('goodnames.txt','r')
writefile.write(r'var neighbData = {"type":"FeatureCollection","features":[')
i = 1
names = [name.strip() for name in file1]
for name in names:
	writefile.write(r'{"type":"Feature","id":"'+ '{0:03g}'.format(i) +'","properties":{"name":"')
	writefile.write(name)
	writefile.write(r'","rank":50.00},"geometry":{"type":"MultiPolygon","coordinates":')
	coord = open(r'Coords/'+name+'.txt').next()
	writefile.write(coord)
	if name == names[-1]:
		print name
		writefile.write(r'}}')
	else:
		writefile.write(r'}},')
	i += 1
	

writefile.write(']};')






#http://leafletjs.com/examples/us-states.js