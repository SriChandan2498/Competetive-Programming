# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k) or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def power(x,y):
    temp = 0
    if( y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp

def powerSum(n, k):
    # Your code goes here...
    if(n<0 or k<0):
        return 0
    Sum = 0
    for i in range(1,n+1):
        Sum += power(i,k)
    return Sum

def test():
    # Write your own test cases here...
    assert powerSum(10, 2)==385,'test case failed'
    assert powerSum(0, 2)==0,'test case failed'
    assert powerSum(10, 0)==10,'test case failed'
    assert powerSum(10, 5)==220825,'test case failed'
    assert powerSum(-10, 5)==0,'test case failed'
    assert powerSum(10, -5)==0,'test case failed'
    print ("All test cases passed...")

test()








