# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	x = dict()
	for i in s:
		if(i not in x):
			x[i] = 1
		else:
			x[i] += 1
	freq = sorted(x.values(),reverse=True)[n-1]
	for i in x:
		if(x[i] == freq):
			return i

fun_kth_occurrences("helllo woorld", 2)
	
	


