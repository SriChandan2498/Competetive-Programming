# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l = len(s)
	if(n > l):
		n %= l
	if(n>0):
		return s[n:]+s[:n]
	elif(n<0):
		return s[l+n:]+s[:l+n]
	else:
		return s

