schoolfile = open('Data/schools.csv','r')

finalfile = open('Data/Final/ssf.csv','w')

for line in schoolfile:
	feats = [i.split() for i in line.split(',')]
	scores = [ int(i[0]) for i in feats[1:] ]
	score = sum(scores)/float(len(scores))
	finalfile.write( feats[0][0] +','+ '{0:.1f}'.format(score) +'\n' )

schoolfile.close()

finalfile.close()