"""
Count the number of times a substring appears in a string
Time complexity: O(n) - n is number of characters in a
Space complexity: O(1)
"""
def substrcount(a, b):
    res = 0
    sub_len = len(b)
    for i in range(len(a)):
        if a[i:i+sub_len] == b:
            res += 1
    return res
        
a = "tabcabceabcnabmcab"
b = "abc"
assert substrcount(a,b) == 3
a = "aaaaaa"
b = "aa"
assert substrcount(a,b) == 5

# solution - 2
# To avoid counting overlap match of substrings
def substrcount(a, b):
    res = 0
    sub_len = len(b)
    i = 0
    while i < len(a):
        if a[i:i+sub_len] == b:
            res += 1
            i = i+sub_len
        else: i += 1
            
    return res
        
a = "tabcabceabcnabmcab"
b = "abc"
assert substrcount(a,b) == 3
a = "aaaaaa"
b = "aa"
assert substrcount(a,b) == 3