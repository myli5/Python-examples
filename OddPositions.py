"""
Write a function that returns the elements on odd positions (0 based) in a list
Time complexity: O(n)
Space complexity: O(n/2)
"""
def oddPos(input):
    output = []
    inputLen = len(input) 
    for i in range(0,inputLen):
       if (i%2 == 1):
         output.append(input[i])       
    return output

assert oddPos([0,1,2,3,4,5]) == [1, 3,5]
assert oddPos([1,-1,2,-2]) == [-1,-2]
