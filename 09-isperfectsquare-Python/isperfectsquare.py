# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

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

# print(isperfectsquare(6.25))