# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
def isPrime(n):
	if(n<2):
		return False
	if(n == 2):
		return True
	if(n%2==0):
		return False
	maxfactor = round(n**0.5)
	for i in range(3,maxfactor+1,2):
		if(n%i==0):
			return False
	return True

def powerfulnumber(n):
    l = []
    for i in range(n):
        if(isPrime(i) and n%i==0):
            l.append(i)
    if(len(l)==0):
        return False
    for i in l:
        if n%(i**2)!=0:
            return False
    return True

def nthpowerfulnumber(n):
	# Your code goes here
	if(n==0):
		return 1
	found = 0
	guess = 0
	while found < n:
		guess += 1
		if(powerfulnumber(guess)):
			found += 1
	return guess