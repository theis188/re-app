#crimemissing
neighbs = open('goodnames.txt')
neighblist = [i.strip() for i in neighbs]
neighbs.close()

vdic = {}
violcrime = open('Data/propcrim.txt')
for line in violcrime:
	feats = line.split(',')
	vdic[feats[0].strip()]=feats[2].strip()

crimers = open('Data/pcf.csv','w')

for i in neighblist:
	if i in vdic.keys():
		towrite = i+','+vdic[i]
	else:
		towrite = i+','+'NULL'
	crimers.write(towrite+'\n')
crimers.close()