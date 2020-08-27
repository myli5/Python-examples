
"""
 Validate Anagrams
Find out if string S is an anagram of string T.
input
S = "the eyes"
T = "they see"
expected output
True
input 2
S = "a gentleman"
T = "elegant man"
expected output
True

Anagram - a word or a phrase formed by
rearranging the letters of another,
such as cinema, formed from iceman.

Time complexity: O(nlogn) because of using sorted (mergesort alg)
"""
def anagrams(S, T):
    # the sorted strings are checked  
    if(sorted(S) == sorted(T)): 
        return True  
    else: 
        return False  

S = "the eyes"
T = "they see"
assert anagrams(S, T) == True
S = "a gentleman"
T = "elegant man"
assert anagrams(S, T) == True

# solution - 2
def anagrams(S, T):
    s_list = list(S)
    s_list.sort()
    t_list = list(T)
    t_list.sort()

    return (s_list == t_list)
S = "the eyes"
T = "they see"
assert anagrams(S, T) == True
S = "a gentleman"
T = "elegant man"
assert anagrams(S, T) == True


# solution - 3
# Time complexity: O(n+m)
NO_OF_CHARS = 256  
# Function to check whether two strings are anagram of 
# each other 
def anagrams(S, T):    
    if len(S) != len(T): 
        return False 
    # Create two count arrays and initialize all values as 0 
    count1 = [0] * NO_OF_CHARS 
    count2 = [0] * NO_OF_CHARS   
    # For each character in input strings, increment count 
    # in the corresponding count array 
    for i in S: 
        count1[ord(i)]+= 1  
    for i in T: 
        count2[ord(i)]+= 1  
    # Compare count arrays 
    for i in range(NO_OF_CHARS): 
        if count1[i] != count2[i]: 
            return False
        
    return True

S = "the eyes"
T = "they see"
assert anagrams(S, T) == True
S = "a gentleman"
T = "elegant man"
assert anagrams(S, T) == True