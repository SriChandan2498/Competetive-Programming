# makeMagicSquare(n)
# Write the function makeMagicSquare(n) that takes a positive 
# odd integer n and returns an nxn magic square by following 
# the resource here. If n is not a positive odd integer, 
# return None.

# URL: https://en.wikipedia.org/wiki/Magic_square

# Hints: From Geeks for Geeks.
# Did you find any pattern in which the numbers are stored? 

# In any magic square, the first number i.e. 1 is 
# stored at position (n/2, n-1). Let this position 
# be (i,j). The next number is stored at position (i-1, j+1) 
# where we can consider each row & column as circular array 
# i.e. they wrap around.

# Three conditions hold:

# 1. The position of next number is calculated by 
# decrementing row number of the previous number by 1,
#  and incrementing the column number of the previous 
# number by 1. At any time, if the calculated row position 
# becomes -1, it will wrap around to n-1. Similarly, if 
# the calculated column position becomes n, it will wrap 
# around to 0.

# 2. If the magic square already contains a number at the 
# calculated position, calculated column position will be 
# decremented by 2, and calculated row position will be 
# incremented by 1.

# 3. If the calculated row position is -1 & calculated 
# column position is n, the new position would be: (0, n-2). 

def makeMagicSquare(n):
    # Your code goes here...
    l = [[0 for x in range(n)] for y in range(n)]
    i = int(n/2)
    j = int(n-1)
    number = 1
    while number <= (n*n):
        if(i<0 and j == n):
            j = n - 2
            i = 0
        if(i < 0):
            i = n - 1
        if(j == n):
            j = 0
        if(l[i][j]!=0):
            j -= 2
            i += 1
            continue
        l[i][j] = number
        number += 1
        j = j + 1
        i = i - 1
    return l

def test():
    # Test Cases
    assert makeMagicSquare(3)==[[2, 7, 6], [9, 5, 1], [4, 3, 8]], "test case failed"
    assert makeMagicSquare(5)==[[9, 3, 22, 16, 15], [2, 21, 20, 14, 8], [25, 19, 13, 7, 1], [18, 12, 6, 5, 24], [11, 10, 4, 23, 17]], "test case failed"
    assert makeMagicSquare(7)==[[20, 12, 4, 45, 37, 29, 28], [11, 3, 44, 36, 35, 27, 19], [2, 43, 42, 34, 26, 18, 10], [49, 41, 33, 25, 
    17, 9, 1], [40, 32, 24, 16, 8, 7, 48], [31, 23, 15, 14, 6, 47, 39], [22, 21, 13, 5, 46, 38, 30]], "test case failed"
    print("All testscases passed")

test()