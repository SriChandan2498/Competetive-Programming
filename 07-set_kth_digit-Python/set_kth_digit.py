# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 


def fun_set_kth_digit(n, k, d):
	x = str(abs(n))
	l = len(x)
	if(l == k):
		x = str(d)+x
	else:
		x = x[:l-k-1]+str(d)+x[l-k:]
	if(n < 0):
		return -1*int(x)
	else:
		return int(x)
print(fun_set_kth_digit(-468, 3, 1))

