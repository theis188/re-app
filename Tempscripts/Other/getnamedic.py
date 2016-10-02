names = open('neighbnames.txt','r')
slugs = open('neighburls.txt','r')

namedic = {}

while True:
	try:
		namedic[slugs.next().strip()] = names.next().strip()
	except:
		break

names.close()
slugs.close()

good = open('goodnames.txt','r')

s = '{'

while True:
	try:
		currslug = good.next().strip()
		s = s +'"'+ currslug +'"'
		s = s + ':'
		s = s +'"'+ namedic[currslug] +'"'
		s = s + ','

	except:
		break
s = s[:-1]
s = s + '}'

open('temp.txt','w').write(s)

