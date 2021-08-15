# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 

def fun_get_kth_digit(digit, k):
	s = str(abs(digit))
	if(len(s) <= k):
		return 0
	x = s[-1*(k+1)]
	if(x.isdigit()):
		return int(x)
	else:
		return 0
