# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

def isperfectsquare(n):
	# your code goes here
	x = None
	if(type(n) == str):
		try:
			x = int(n)
		except:
			return False
	x = int(n)
	if(x < 0):
		return False
	y = (x)**0.5
	if(y-int(y) == 0):
		return True
	else:
		return False
	
def largestperfectsquare(n):
	# your code goes here
	if(isperfectsquare(n)):
		return n
	x = n
	while(x > 0):
		if(isperfectsquare(x)):
			return x
		x -= 1
	