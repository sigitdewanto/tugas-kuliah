import re

grammars = { "S_1" : ("Cari","<Judul>","Dalam","<Format>"), "S_2" : ("Cari","<Judul>") }

##parser
def judul(value):
	regex = re.compile('[\w\s]+\s*',re.IGNORECASE)
	if regex.match(value) != None:
		return True
	return False

def format(value):
	value = value.lower();
	if value == "buku" or value == "jurnal" or value == "prosiding":
		return True
	return False

def parse_token(token):
	result = -1
	for k in grammars:
		grammar = grammars[k]
		if(len(token)==len(grammar)):
			i = 0
			value = [None] * len(token)
			for i in xrange(0,len(token)):
				if grammar[i].lower() == "cari" and i ==0:
					if token[i].lower()=="cari":
						value[i] = 1
				elif grammar[i].lower() == "<judul>" and i == 1:
					if judul(token[i].lower()):
						value[i] = 1
				elif grammar[i].lower() == "dalam" and i == 2:
					if token[i].lower()=="dalam":
						value[i] = 1
				elif grammar[i].lower() == "<format>" and i == 3:
					if format(token[i].lower()):
						value[i] = 1
			result = 1
			for i in xrange(0,len(token)):
				if value[i] == 0 or value[i] == None:
					print "{} is not match {}, because \n{} is not match with its grammar {}".format(token,grammar,token[i],grammar[i])
					print "\n"
					result = 0;
			if result==1:
				print "{} is match {}".format(token,grammar)
				print "\n"
		else:
			print "{} is not match {}".format(token,grammar)
			print "\n"


example_token = {0:("Cari", "Natural Language Processing", "Dalam","Buku"),1:("Tidak", "Natural Language Processing", "Dalam"),2:("Dalam","Tes tes")}

for token in example_token:
	parse_token(example_token[token])


