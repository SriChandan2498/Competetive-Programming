# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if(a == []):
		return -1
	diff = set()
	n = len(a)
	for i in range(n):
		for j in range(i+1,n):
			diff.add(abs(a[i] - a[j]))
	return min(diff)

smallestdifference([19,2,83,6,27])