class processor():
	def __init__(self):
		self.names = ["prop-crime", 
		"viol-crime",
		"air-qual",
		"school-qual",
		"pop-dens-h",
		"pop-dens-l",
		"rest-dens",
		"buy-price",
		"rent-price",
		"walk-score"]

		self.namedic = {"prop-crime":"pcf", 
		"viol-crime":"vcf",
		"air-qual":"aqf",
		"school-qual":"sqf",
		"pop-dens-h":"pdf",
		"pop-dens-l":"pdf",
		"rest-dens":"rdf",
		"buy-price":"hpf",
		"rent-price":"rpf",
		"walk-score":"wsf"}

	def openfiles(self):
		self.files = {}
		for name in set( self.namedic.values () ):
			self.files[name] = open('Data/Final/Normal/'+name+'.csv','r')

	def writefile(self):
		writefile = open('Data/Final/Normal/final.csv','w')
		while True:
			linenum = {}
			for name in set( self.namedic.values () ):
				linenum[name] = self.files[name].next().split(',')[1].strip()
			nums = [ ( linenum[ self.namedic[name] ] if name!='pop-dens-l' else '{0:.1f}'.format ( 100.0 - float (linenum[ self.namedic[name] ] ) ) ) for name in self.names  ]
			linewrite = ','.join( nums )
			writefile.write(linewrite+'\n')

inst = processor()
inst.openfiles()
inst.writefile()