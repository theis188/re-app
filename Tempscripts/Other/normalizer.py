import math

def standard(n):
	return n

def neglog(n):
	return -math.log(n)

def neg(n):
	return -n

def dataread(stem,fund):
	ret = ''
	loc = 'Data/Final/'+stem+'.csv'
	fun = fund[stem]
	datafile = open(loc,'r')
	featdic = {}
	for line in datafile:
 		feats = line.split(',')
 		featdic[feats[0].strip()] = fun(float(feats[1].strip()))
 	datafile.close()
 	vals = featdic.values()
 	minval = min(vals)
 	maxval = max(vals)
 	orderfile = open('goodnames.txt','r')
 	for line in orderfile:
 		name = line.strip()
 		rankscore = ( featdic[name] - minval)/( maxval - minval ) * 100.0
 		ret = ret + name +','+ '{0:.1f}'.format(rankscore) +'\n'
 	orderfile.close()
 	return ret

fundic = {
	'aqf':neg,
	'hpf':neglog,
	'pcf':neg,
	'pdf':standard,
	'rdf':standard,
	'sqf':standard,
	'vcf':neg,
	'wsf':standard,
}

for stem in fundic:
	towrite = dataread(stem,fundic)
	formfile = open('Data/Final/Normal/'+stem+'.csv','w')
	formfile.write(towrite)
	formfile.close()