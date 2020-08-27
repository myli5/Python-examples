"""
Friends Pair Tree count
Count of Friends
Given the edge set of a graph, 
count for each person the number of his friends.
Return a dictionary {person: count_of_friends}.
input[["A", "B"], ["B", "C"], ["B", "D"], ["E"]] 
# A and B , B and C, B and D are friends. 
E (or any nodethat's a single element in the list) 
has no friend.
output (dict): {A:1, B: 3, C:1, D:1, E:0}

Time complexity: O(N)
Space complexity: O(2N) - one for set and one dict
"""
from collections import defaultdict
def solution(input):
    res = defaultdict(int)
    mset = set()
    for rel in input:
        if len(rel) >1:
            if ((rel[0] != rel[1]) and \
                (rel[0],rel[1]) not in mset and  \
                (rel[1],rel[0]) not in mset ):            
                res[rel[0]] += 1
                res[rel[1]] += 1
                mset.add((rel[0],rel[1]))      
        elif (len(rel) == 1):
            res[rel[0]] = 0
    
    return str(dict(res)).replace("'","")
    
assert solution([["A", "B"], ["B", "C"], ["B", "D"], ["E"]])\
 == str("{A: 1, B: 3, C: 1, D: 1, E: 0}")
assert solution([["A", "B"], ["B", "C"], ["C","B"], ["B", "D"], ["E"]])\
 == str("{A: 1, B: 3, C: 1, D: 1, E: 0}")