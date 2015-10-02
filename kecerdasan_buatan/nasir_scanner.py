elemen_terminal = ("cari","dalam","buku","jurnal","prosiding")

def scan_sentence(sentence):
	result = 0
	for i in xrange(0,len(elemen_terminal)):
		if elemen_terminal[i] in sentence.lower():
			result+=1
	if result > 0:
		return True
	return False

def build_token(sentence):
	token_temp = sentence.split()
	temp_string = None
	output_token = []
	for i in xrange(0,len(token_temp)):
		if temp_string is None:
			if scan_sentence(token_temp[i]):
				output_token.append(token_temp[i])
			else:
				temp_string = token_temp[i]
		else:
			if scan_sentence(token_temp[i]):
				output_token.append(temp_string)
				temp_string = None
				output_token.append(token_temp[i])
			else:
				temp_string += " " + token_temp[i]
	if temp_string is not None:
		output_token.append(temp_string)
	return output_token

example_sentence = ("cari matematika dalam buku","matematika buku dalam cari","cuma testing","dalam buku","cari matematika fuzzy dalam jurnal")

for i in xrange(0,len(example_sentence)):
	if scan_sentence(example_sentence[i]):
		print "{} is converted to this token {}".format(example_sentence[i],build_token(example_sentence[i]))
	else:
		print "{} is probably not in our grammar".format(example_sentence[i])
