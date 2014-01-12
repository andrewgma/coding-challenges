escape_char = 'y'
delimiter = 'z'

def encode(strings):
	output = ''
	for string in strings:
		for char in string:
			if char == escape_char or char == delimiter:
				output += 'y'
			output += char
		output += 'z'
	return output

def decode(string):
	output = []
	cur_word = ''
	skip_next = False
	for i in range(len(string)):
		if skip_next:
			skip_next = False
			continue
		if string[i] == escape_char:
			skip_next = True
			cur_word += string[i+1]
		elif string[i] == delimiter:
			output.append(cur_word)
			cur_word = ''
		else:
			cur_word += string[i]
	return output

strings = ['azzzzzzzzz', 'zzzzzzzzzzz','b','cdefghijklmnop']
encoded = encode(strings)
print encoded
print decode(encoded)
