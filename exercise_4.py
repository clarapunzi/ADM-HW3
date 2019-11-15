# The following function returns by recursion the length L of the longest palindromic substring of a given string s

def lps(s):
    n = len(s)
    
    # basic cases: L = 0 if s is an empty substring, L = 1 if s has only one character
    
    if n == 0 or n == 1:         
        L = n
    
    # the recursion goes as follows: if the first and last character of the string are the same, then it is sufficient to add 2 to the length     
    # of the longest palindromic substring of the same string deprived of the first and last character, i.e. s[1:-1]; if not, then it is the       
    # maximum between the length of the longest palindromic substring of s[:-1] and that of s[1:]
    
    else:
        if s[0] == s[-1]:          
            return 2+lps(s[1:-1])
        else:
            return max(lps(s[:-1]), lps(s[1:]))
    return L

# This solution is not optimal because it is very likely to happen that the function lps(s) will be called on the same substring in different branches of the recursion.
# A possible way to improve might be to store the result of each call, so that, instead of calling the function again, everytime we will get a substring that has already appeared 
# we just select the value of its longest palindrome substring among the ones that are stored.
