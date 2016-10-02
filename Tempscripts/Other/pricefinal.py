def mult(x,y): return x*y

def geomean(arr):
	n = len(arr)
	prod = reduce(mult,arr)
	return prod ** (1/ float(n) )

pricefile = open('Data/prices.csv','r')

finalfile = open('Data/final/hpf.csv','w')

for line in pricefile:
	feats = [i.strip() for i in line.split(',')]
	feats = [i for i in feats if i != 'None']
	rowprs = [ int(i) for i in feats[1:] ]
	pr = geomean(rowprs)
	finalfile.write(feats[0]+','+'{0}'.format( str( (pr//1000) * 1000 )  ) + '\n' )

pricefile.close()
finalfile.close()