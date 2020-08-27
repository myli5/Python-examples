"""
Write a function that returns the cumulative sum of elements in a list
Time complexity: O(n)
Space complexity: O(n)
"""
def csum(input):
    output =[]
    sum = 0
    for x in input:
      sum += x
      output.append(sum)   

    return output

assert csum([1,1,1]) == [1,2,3]
assert csum([1,-1,3]) == [1,0,3]
