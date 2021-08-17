# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.
import numpy as np

def fun_matrixmultiply(m1, m2):
    r1,c1,r2,c2 = len(m1),len(m1[0]),len(m2),len(m2[0])
    if(c1 != r2):
        return None
    res = [[0 for i in range(c2)] for i in range(r1)]
    # print(res)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j] += m1[i][k] * m2[k][j]
    return res

print(fun_matrixmultiply([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]]))




