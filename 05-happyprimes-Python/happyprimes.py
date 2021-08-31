# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def sumOfSquaresOfDigits(n):
    res = 0
    while(n > 0):
        res += (n%10)**2
        n //= 10
    return res

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n%2 == 0):
        return False
    for i in range(3,round(n**0.5)+1,2):
        if(n%i == 0):
            return False
    return True

def ishappyprimenumber(n):
    # Your code goes here
    if(not isPrime(n)):
        return False
    seen = set()
    seen.add(n)
    num = n
    while num!=1:
        sos = sumOfSquaresOfDigits(num)
        if(sos in seen or sos==4):
            return False
        seen.add(sos)
        num = sos
    return True


# print(sumOfSquaresOfDigits(123))