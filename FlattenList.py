"""
Write a function that takes a nested list and flattens to a regular list
Time complexity: O(n) - n is the number of elements in the list
Space complexity: O(n) 
"""
def flatList(input):
    output=[]
    for items in input:
        if type(items)==int: output.append(items)
        else: output += flatList(items)
    return output

assert flatList([1, 2, 3, [4, 5, [6, 7], [8]], [9,10]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]