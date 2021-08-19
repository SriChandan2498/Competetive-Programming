# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(n):
    if(n<2):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    mf=round(n**0.5)
    for i in range(3,mf+1,2):
        if(n%i==0):return False
    return True
    
def sumofdigits(m):
    sod=0
    while(m>0):
        rem=m%10
        sod=sod+rem
        m=m//10
    return sod

def isaddtprime(p):
    b=isprime(p)
    a=sumofdigits(p)
    if(b):
        if(isprime(a)):
            return True
    else:
        return False

def fun_nth_additive_prime(x):
    j=2
    found=-1
    while(True):
        q=isaddtprime(j)
        if(q==True):
            found+=1
        if(found==x):
            return j
        j+=1



	