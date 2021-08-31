# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def isProperty309(n):
	p = n**5
	s = str(p)
	for i in range(10):
		if str(i) not in s:
			return False
	return True

def nthwithproperty309(n):
	# Your code goes here
	found = 0
	guess = 0
	while found <= n:
		guess += 1
		if isProperty309(guess):
			found += 1
	return guess