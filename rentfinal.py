
def cash(n):
	digs = len(n.split('.')[0])
	commas = (digs-1)//3
	a =  n.split('.')[0] [::-1]
	listly = [ a[i*3:(i+1)*3] for i in range(commas+1)]
	num=','.join(listly)[::-1]
	ret = '$'+num+'.00'
	return ret

rentfile = open('Data/rents.csv')
s = '{'

for line in rentfile:
	feats = line.split(',')
	feats.split
	s=s+
	