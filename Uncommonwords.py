
"""
Uncommon words
Find the uncommon words between two strings
Find out the disjointed set of words in two strings.
input
s1 = "Thank you for the present! "
s2 = " Thanks for the gift"
expected output
["Thank", "Thanks", "you", "present!", "gift"]
Corner cases:
1. How to handle duplicated words in one of the strings.
s1 = "hello hello"
s2 = "hello"
In this case what is the disjointed set?
2. Empty String and None values
3. Is upper-case letter considered the same as its lower case?

Time complexity: O(n+m)
Space complexity: O(n+m) for dictionary
"""
# solution 1
def uncommonWords(A, B): 
    #A=A.casefold()
    #B=B.casefold()
    count = {}   
    for word in A.split(): 
        count[word] = count.get(word, 0) + 1      
    # insert words of string B to hash 
    for word in B.split(): 
        count[word] = count.get(word, 0) + 1  
    # return required list of words 
    return [word for word in count if count[word] == 1] 
  
A = "Thank you for the present! "
B = " Thanks for the gift"  
assert uncommonWords(A, B) == ['Thank', 'you', 'present!', 'Thanks', 'gift']

s1 = "hello hello"
s2 = "hello"
assert uncommonWords(s1,s2) == []

# solution - 2
# Time complexity for ^ operation is O(len(a))
def uncommonWords(a,b): 
    a=a.split() 
    b=b.split() 
    k=set(a)^(set(b)) 
    return k