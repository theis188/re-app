import re

hpf = open('../../Data/Final/Format/rpf.csv')
s = '{'

for line in hpf:
	search = re.search(r'([a-z-]+),([\$,0-9\.a-z /]+)',line)
	s = s+'"' + search.group(1) + '"'
	s = s + ':'
	s = s+'"' + search.group(2) + '"' + ','

s = s[:-1]
s = s+'}'

open('tempt.txt','w').write(s)