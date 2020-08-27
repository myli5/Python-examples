"""
Letter count
Count the letter character, c in a given string
Time complexity: O(n)
Space complexity: O(1)
n is the number of characters
"""
def count(s, c) : 
    res = 0     
    for i in range(len(s)) : 
        if (s[i] == c): 
            res = res + 1
    return res 

assert count('mississippi','s') == 4