# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def alternatingsum(l,i,res=0):
	if(l == []):
		return res
	else:
		res += ((-1)**i)*l[0]
		return alternatingsum(l[1:],i+1,res)

def fun_recursions_alternatingsum(l): 
	return alternatingsum(l,0)