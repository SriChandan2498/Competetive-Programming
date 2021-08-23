# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def getEvenDigits(n,i=0,x=0):
    if(n == 0):
        return x
    else:
        rem = n%10
        if(rem % 2 == 0):
            x += rem*(10**(i))
            i+=1 
        return getEvenDigits(n//10,i,x)
        
def onlyEvenDigitsHelper(l,res=[]):
    if(l == []):
        return res
    else:
        res.append(getEvenDigits(l[0]))
        return onlyEvenDigitsHelper(l[1:],res)

def fun_recursion_onlyevendigits(l):
	if(l == []):
		return []
	return onlyEvenDigitsHelper(l,[])