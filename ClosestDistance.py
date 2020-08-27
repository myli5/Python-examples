"""
Closest Distance
Find the closest distance between two words that are the same. Any non-alphanumeric character is
treated as a delimiter between words. Therefore "wasn't" is two words "wasn" and "t". The solution
should be case-insensitive.
input
“I felt happy because I saw the others were happy and because I knew I should feel happy, but I
wasn’t really happy”
output 1
#the closest identical words => ‘I’ and ‘I’. They are one word array from each other with the word
"knew" in between

Time complexity: O(n)
Space complexity: O(n)
"""
import re
def closestDist(S) -> int:
    S = S.lower()
    words = re.split(r'[ ,\']',S)
    d = dict()
    min_dist = len(words)
    for i in range(len(words)):
        if words[i] in d:
            last_occur = d[words[i]]
            if i - last_occur < min_dist:
                min_dist = i - last_occur -1

        d[words[i]] = i

    return min_dist

input = " I felt happy because I saw others were happy and because I knew I should feel happy, but I wasn't really happy"
assert closestDist(input) == 1