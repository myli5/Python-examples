"""
Common words in two strings
# solution here is case sensitive
"""
def commonWords(a, b):
    set1 = set(a.split())
    set2 = set(b.split())
    common = sorted(list(set1 & set2))
    return common

a = "Thank you so much"
b = "Happy, Thank you"
assert commonWords(a,b) == ['Thank', 'you']