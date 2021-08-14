# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
def almostEqual(a,b):
	return abs(a-b) <= 10**-9

def getslope(a1,b1,a2,b2):
	return (a2-a1)/(b2-b1)

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	m1 = getslope(x1,y1,x2,y2)
	m2 = getslope(x2,y2,x3,y3)
	m3 = getslope(x3,y3,x1,y1)
	if(almostEqual(m1*m2,-1) or almostEqual(m2*m3,-1) or almostEqual(m3*m1,-1)):
		return True
	return False	