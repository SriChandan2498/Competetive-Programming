# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.
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
   

def fun_nearestkaprekarnumber(n):
    guess1 = 0
    guess2 = 0
    i = 0
    while True:
        if(isKaprekarNumber(n-i) and guess1==0):
            guess1 = n-i
            if(guess2!=0):
                break
        if(isKaprekarNumber(n+i) and guess2==0):
            guess2 = n+i
            if(guess1!=0):
                break
        i += 1
    if((abs(n-guess1)==abs(n-guess2)) or (abs(n-guess1)<abs(n-guess2))):
        return guess1
    return guess2
    