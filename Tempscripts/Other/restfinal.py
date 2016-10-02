finalfile = open('Data/Final/rdf.csv','w')
restfile = open('Data/restaurants.csv','r')
for line in restfile:
	feats = line.split(',')
	rests = [float( i ) for i in feats[1:] ]
	meters = rests.pop()
	avrests = sum(rests)/len(rests)
	mirests = avrests / 3.14158 / (350**2) / ( 3.281**2 ) * (5280**2)
	
	finalfile.write(feats[0]+','+'{0:.1f}'.format(mirests)+'\n')