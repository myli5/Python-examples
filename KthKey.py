"""
kth Key in a set - 
Find out the Kth largest key in a set. Compare each element by the letter in the tuple.
case 1) input
s = {('h', 5), ('r', 6), ('b', 2), ('a', 10), ('f', -4), ('g', 0)}
k = 3
expected output
f
case 2) input
s = {('a',2),('b',3),('c',1)} 
k = 2
expected output
b
case 3) input
s = {('a', 1), ('c', 2), ('b', 3)}
k = 4
expected output
None
case 4) input
s = {}
k = 1
expected output
None

Time complexity for sorted is O(nlogn)
"""
def kthKey(s : set, k : int) -> tuple:
    if k > len(s):
        return None
    ls=list(s)
    ls = sorted(ls) #O(nlogn)
    return ls[k - 1][0]
    
assert kthKey({('h', 5), ('r', 6), ('b', 2), ('a', 10), ('f', -4), ('g', 0)}, 3) == 'f'
assert kthKey({('a',2),('b',3),('c',1)},2) == 'b'
assert kthKey({('a', 1), ('c', 2), ('b', 3)}, 4) == None
assert kthKey({}, 1) == None
