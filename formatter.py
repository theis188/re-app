
def aqi(n):
 	return n + ' ' + 'AQI'

def cash(n):
	digs = len(n.split('.')[0])
	commas = (digs-1)//3
	a =  n.split('.')[0] [::-1]
	listly = [ a[i*3:(i+1)*3] for i in range(commas+1)]
	num=','.join(listly)[::-1]
	ret = '$'+num+'.00'
	return ret

def rent(n):
	return cash(n) + ' / month'

def crime(n):
	return n+' / 10k pop / yr'

def dens(n):
	return n+' / sq mi'

def school(n):
	return n+' out of 10'

def walk(n):
	return n+' out of 100'

def dataread(stem,fund):
	ret = ''
	loc = 'Data/Final/'+stem+'.csv'
	fun = fund[stem]
	datafile = open(loc,'r')
	featdic = {}
	for line in datafile:
 		feats = line.split(',')
 		featdic[feats[0].strip()] = feats[1].strip()
 	datafile.close()
 	orderfile = open('goodnames.txt','r')
 	for line in orderfile:
 		name = line.strip()
 		ret = ret + name +','+fun(featdic[name])+'\n'
 	orderfile.close()
 	return ret

fundic = {
	'aqf':aqi,
	'rpf':rent,
	'hpf':cash,
	'pcf':crime,
	'pdf':dens,
	'rdf':dens,
	'sqf':school,
	'vcf':crime,
	'wsf':walk,
}

for stem in fundic:
	towrite = dataread(stem,fundic)
	formfile = open('Data/Final/Format/'+stem+'.csv','w')
	formfile.write(towrite)
	formfile.close()