# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2
import math

def ispalindrome(n):
	x = str(n)
	return x == x[::-1]

def isprime(n):
	if(n < 2):
		return False
	if(n == 2):
		return True
	if(n % 2 == 0):
		return False
	m = int(math.sqrt(n))+1
	for i in range(3,m,2):
		if(n%i == 0):
			return False
	return True

def fun_nth_palindromic_prime(n):
	i = 2
	count = -1
	while(True):
		if(ispalindrome(i) and isprime(i)):
			count += 1
		if(count == n):
			return i
		i += 1
