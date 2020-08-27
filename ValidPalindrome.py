"""
valid polindrome
Find whether given string is a palindrome or not
Time complexity: O(n)
Space complexity: O(1)
"""
# solution 1 
def isPalindrome(s):
    x = ""
    diff = ord('a') - ord('A') #ord -unicode code of a specified character.
    for i in s:
        if ord(i)>=ord('a') and ord(i)<=ord('z') or \
           ord(i)>=ord("0") and ord(i)<=ord("9"):
            x+=i
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            i = chr(diff+ord(i))
            x+=i

    return x == x[::-1]
                                                                              
assert isPalindrome("A Man, a Plan, a Canal: Panama") == True

#solution 2
def isPalindrome2(s): 
    fchars = filter(lambda ch: ch.isalnum(), s)
    lfchars = map(lambda ch: ch.lower(), fchars)
    fchars_list = list(lfchars)
    rchars_list = fchars_list[::-1]

    return fchars_list == rchars_list

assert isPalindrome2("A Man, a Plan, a Canal: Panama") ==True
