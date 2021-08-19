# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def getprimefactors(n):
	primefactors = list()
	# if(n%2 == 0):
	# 	primefactors.add(2)
	while(n%2 == 0):
		primefactors.append(2)
		n = n // 2
	for i in range(3,int(math.sqrt(n))+1,2):
		if(n%i == 0):
			primefactors.append(i)
			n = n//i
	if(n>2):
		primefactors.append(n)
	return primefactors
def ispowerfulnumber(n):
	primefactors = set(getprimefactors(n))
	# print(primefactors)]
	for i in primefactors:
		if(n % (i)**2 != 0):
			return False
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	if(n == 0):
		return 1
	i = 1
	count = 0
	while(True):
		if(ispowerfulnumber(i)):
			count += 1
		if(count == n):
			return i
		i += 1
print(nthpowerfulnumber(53)) 
