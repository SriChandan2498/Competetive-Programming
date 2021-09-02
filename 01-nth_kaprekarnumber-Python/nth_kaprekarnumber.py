# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def isKaprekarNumber(number):
    n = int(math.pow(number,2))
    s = str(n)
    if(number==1):
        return True
    for i in range(1,len(s)):
        Sum = 0
        check = int(math.pow(10, i))
        if(number==check):
            return False
        Sum = int(s[:i]) + int(s[i:])
        if Sum == number:
            return True
    return False

def fun_nth_kaprekarnumber(n):
	found = -1
	guess = 0
	while found < n:
		guess += 1
		if(isKaprekarNumber(guess)):
			found += 1
	return guess