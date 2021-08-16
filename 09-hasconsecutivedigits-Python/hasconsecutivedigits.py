# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	x = str(abs(n))
	prev = ''
	for i in range(len(x)-1):
		if(x[i] == x[i+1]):
			return True
	return False