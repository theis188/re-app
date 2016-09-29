
pricefile = open('Data/prices.csv','r')

finalfile = open('Data/final/hpf.csv','w')

for line in pricefile:
	feats = [i.strip() for i in line.split]