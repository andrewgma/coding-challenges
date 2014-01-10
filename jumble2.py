# see if each word in the dictionary can be written using letters in the input word
def solve(word, dict):
	output = []
	letters = {}
	for letter in word:
		if letter in letters:
			letters[letter] += 1
		else:
			letters[letter] = 1
	for possible in dict:
		add = True
		available = letters.copy()
		for letter in possible:
			if letter in available and available[letter] > 0:				
				available[letter] -= 1
			else:
				add = False
		if add:
			output.append(possible)
	return output

# source: 12Dicts from http://wordlist.sourceforge.net/
f = open('2of12.txt', 'rb')
dict = []
for line in f:
	dict.append(line.rstrip())

print solve("knee", dict)