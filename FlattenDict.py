"""
Write a function that takes a nested dictionary and flattens to a regular dictionary
Time complexity: O(n) - number of key/val items
Space complexity: O(n)
"""
def flatDict(input):
    output = {}
    for key, val in input.items():
        if type(val) == dict:
            output[key] = len(input.keys())
            output.update(val)
        else:output[key] = val 
            
    return output

assert flatDict({'a' : 1, 'b' : {'c': 3, 'd': 4}}) == dict(a=1, b=2, c=3, d=4)