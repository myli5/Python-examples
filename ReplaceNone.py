"""
Replace None - Write a function that takes a list of input values where it replaces the None values with previous number value.
Time complexity: O(n) 
Space complexity: O(1)
"""
def replaceNone(ls):
    if (len(ls) == 0):
        return []
    prev = None
    for i in range(len(ls)):
        if ls[i]:
            prev = ls[i]
        else:
            ls[i] = prev
    if not prev:
        return []
    return ls

assert replaceNone([1, None, 2, None, 3, None, None, 5, None]) == [1, 1, 2, 2, 3, 3, 3, 5, 5]
assert replaceNone([None, None, 8, None]) == [None, None, 8, 8]
assert replaceNone([None]) == []