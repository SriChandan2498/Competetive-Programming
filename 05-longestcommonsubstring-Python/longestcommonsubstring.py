# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    s = ""
    count = 0
    l = []
    for i in range(len(s1)):        
        if s1[i] not in s2:
            s = ""
            continue
        s += s1[i]
        if s not in s2:
            s = s[1:]
        if s not in s2:
            continue
        if len(s)>=count:
            count = len(s)
            l.append(s)
    cl = [i for i in l if len(i)==count]
    if cl==[]:
        return ""
    lcs = "" + cl[0]
    for i in cl:
        if i<lcs:
            lcs = i
    return lcs
