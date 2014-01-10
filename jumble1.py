# helper function to get permutations recursively
def helper(head, tail):
	possible = set()
	if len(tail) == 1:
		return set([head + tail])
	else:
		for pos in range(len(tail)):
			possible.add(head + tail[pos])
			word = helper(head + tail[pos], tail[:pos] + tail[(pos+1):])
			possible = possible.union(word)
		return possible

# calls helper function and returns permutations which are English words
def solve(word, dict):
	sol = []
	possible = helper("", word)	
	for word in possible:
		if word in dict:
			sol.append(word)
	return sol

# source: 12Dicts from http://wordlist.sourceforge.net/
f = open('2of12.txt', 'rb')
dict = []
for line in f:
	dict.append(line.rstrip())

print solve("knee", dict)