# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    d = dict()
    for i in lst:
        temp = i
        for j in range(len(lst[0])):
            temp2 = i[:j] + i[j+1:]
            if (i[j] in temp2):
                return False
            if j in d:
                if(i[j] in d[j]):
                    return False
                else:
                    d[j].append(i[j])
            else:
                d[j] = [i[j]]
    return True

def testlatinsquares():
    assert isLatinSquare([['A','B','C'],['C','A','B'],['B','C','A']])==True
    assert isLatinSquare([[1,2,3],[2,3,1],[3,1,2]])==True
    assert isLatinSquare([['A','B','C'],['C','A','B'],['A','C','B']])==False
    assert isLatinSquare([['A','B'],['A','A']])==False
    print("All testcases passed")

testlatinsquares()