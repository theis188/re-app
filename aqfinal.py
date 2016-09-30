import os
basepath = 'Data/AQI'
files = os.listdir(basepath)
print files

airdic = {}

for file in files:
	z = 1
	aqfile = open(basepath+'/'+file)
	for line in aqfile:
		if not (z in airdic):
			airdic[z] = [line.split(',')[-1].strip() ]
		else: 
			airdic[z].append(line.split(',')[-1].strip() )
		z += 1
aqfile.close()

print airdic

avgdic = {}
for z in airdic:
	aqis = [float(j) for j in airdic[z]]
	aqi = sum(aqis)/ len(aqis) 
	avgdic[z] = '{0:.1f}'.format(aqi)

print avgdic

neighbfile = open('Data/aqzones.csv','r')
finalfile = open('Data/Final/aqf.csv','w')

for line in neighbfile:
	feats = line.split(',')
	neighby = feats[0].strip()
	score = avgdic[ int( feats[1].strip() ) ]
	finalfile.write( neighby +','+ score+'\n' )

finalfile.close()
neighbfile.close()