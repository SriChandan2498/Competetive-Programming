# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	asc = None
	n = len(a)
	if(n <= 1):
		return True
	flag = 0
	if(all(a[i] <= a[i + 1] for i in range(n-1)) or all(a[i] >= a[i + 1] for i in range(n-1))):
		flag = 1
	if(flag):
		return True
	return False