# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
import math

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

def sumof_sqr_dig(x):
    sqsum=0
    while(x>0):
        r=x%10
        sqsum=sqsum+(r**2)
        x=x//10
    return sqsum

def ishappyno(y):
    while(True):
        if(y==1):
            return True
        y=sumof_sqr_dig(y)
        if(y==4):
            return False
    return False
        

def fun_nth_happy_prime(n):
	f=-1
	j=2
	while(True):
		if(isprime(j) and ishappyno(j)):
			f+=1
		if(f==n):
			return j
		j+=1