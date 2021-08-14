# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	x = str(n)
	di = dict()
	maxfreq = 0
	for i in x:
		if(i in di):
			di[i] += 1
		else:
			di[i] = 1
		if(di[i] >= maxfreq):
			maxfreq = di[i]
	# print(di,maxfreq)
	res = set()
	for i in di:
		if(di[i] == maxfreq):
			res.add(int(i))
	return min(res)

print(mostfrequentdigit(5231123123123))