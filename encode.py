def get_len_code(string):
	str_length = str(len(string))
	output = ''
	for char in str_length:
		output += lookup[char]
	return output

def get_int_from_code(string):
	reverse_dict = {v: k for k, v in lookup.items()}
	output = 0
	exponent = 0
	for char in string[::-1]:
		output += int(reverse_dict[char]) * 10**exponent
		exponent += 1
	return output

def encode(strings):
	output = ''
	for string in strings:
		output += get_len_code(string) + 'z' + string
	return output

def decode(string):
	output = []
	cur_len_int = 0
	cur_len_str = ''
	cur_str = ''

	for char in string:
		if cur_len_int > 0:
			cur_str += char
			cur_len_int -= 1
		elif len(cur_str) > 0:
			output.append(cur_str)
			cur_str = ''
			cur_len_str += char
		elif char != 'z':
			cur_len_str += char
		elif char == 'z':
			cur_len_int = get_int_from_code(cur_len_str)
			cur_len_str = ''
	output.append(cur_str)
	return output


lookup = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '0':'j'}
strings = ['azzzzzzzzz', 'zzzzzzzzzzz','b','cdefghijklmnop']
encoded = encode(strings)
print encoded
print decode(encoded)
