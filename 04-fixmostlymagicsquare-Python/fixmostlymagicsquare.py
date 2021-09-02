# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def getrowandsum(L):
	sums = [sum(i) for i in L]
	d = {}
	for i in L:
		Sum = sum(i)
		if Sum in d:
			d[Sum] += 1
		else:
			d[Sum] = 1
	counts = [d[i] for i in sums]
	rowtofix = counts.index(min(counts))
	correctsum = sums[0]
	if rowtofix == 0:
		correctsum = sums[1]
	return rowtofix,correctsum

def missingnumber(s,L):
	missing = 0
	for i in range(1,(len(L)**2)+1):
		if i not in s:
			missing = i
	return missing

def fixmostlymagicsquare(L):
	# Your code goes here
	rowtofix,correctsum = getrowandsum(L)
	s = set()
	for i in L:
		s2 = set(i)
		s = s|s2
	missing = missingnumber(s,L)
	for i in range(len(L[rowtofix])):
		temp = [] + L[rowtofix]
		temp[i] = missing
		if sum(temp) == correctsum:
			L[rowtofix] = temp
	return L