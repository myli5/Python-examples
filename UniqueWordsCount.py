"""
Count the number of unique words in a sentence
Input:"this is a test sentence"
Output: 5 
"""
def wordUniqcount(s):
    return len(set(s.split()))
 
assert wordUniqcount("this is a test sentence")== 5
