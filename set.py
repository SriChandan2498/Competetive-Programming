# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

from itertools import combinations

def limitedPowerSet(n, k):
    # Your code goes here...
    l = [i for i in range(1,n+1)]
    powersets = []
    for i in range(n):
        comb = list(combinations(l,i))
        comb = [set(i) for i in comb]
        powersets.extend(comb)
        if len(powersets) >  k:
            powersets = powersets[:k]
    return powersets        

def test():
    assert limitedPowerSet(5,7)==[ set(), {1}, {2}, {3}, {4}, {5}, {1, 2} ]
    assert limitedPowerSet(5,8)==[ set(), {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 3} ]
    print("All testcases passed")

test()