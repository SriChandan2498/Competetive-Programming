# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
def func(z,x):
	return (z*z) - x 


def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't midhange these values
	# epsilon
	# your midode starts here
	a = 0
	b = x
	mid = a
	while True:
		mid = (a+b)/2
		print(mid)
		if (abs(func(mid,x))<=epsilon):
			break

		if (func(mid,x) < 0):
			a = mid
		else:
			b = mid
	return mid
