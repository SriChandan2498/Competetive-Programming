# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    if(n < 2):
        return False
    if(n == 2):
        return True
    if(n%2 == 0):
        return False
    for i in range(3,round(n**0.5)+1,2):
        if(n%i == 0):
            return False
    return True

def getPrimeFactors(n):
    res = list()
    while(n%2 == 0):
        res.append(2)
        n //= 2
    for i in range(3,round(n**0.5)+1,2):
        while n % i== 0:
            res.append(i)
            n = n // i
    if n > 2:
        res.append(n)
    return res

def getsum(n):
    print(list(str(n)))
    return sum(map(int,list(str(n))))

def isSmithNumber(n):
    if(not isPrime(n) and (getsum(n) == sum([getsum(i) for i in getPrimeFactors(n)]))):
        return True
    return False

def fun_nth_smithnumber(n):
    count = -1
    i = 0
    while(count < n):
        i += 1
        if(isSmithNumber(i)):
            count += 1
    return i

print(getsum(123))