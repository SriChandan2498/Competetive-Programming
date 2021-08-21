"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    lo,hi = 0,len(input_array)-1
    while(lo<=hi):
        mid = lo + (hi-lo)//2
        if(value < input_array[mid]):
            hi = mid-1
        elif(value > input_array[mid]):
            lo = mid+1
        else:
            return mid
    return -1
    
        

