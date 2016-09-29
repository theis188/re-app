#crimemissing

wdic = {}
walkfile = open('Data/walkbiketrans.csv','r')
finalfile = open('Data/Final/wsf.csv','w')
for line in walkfile:
	feats = line.split(',')
	if feats[1]=='walk':
		scores = [int(i) for i in feats[2:] if i.strip()]
		avg_score = sum(scores)/float(len(scores))
		finalfile.write( feats[0] +','+ '{0:.1f}'.format(avg_score) + '\n' )

finalfile.close()
walkfile.close()