"""
centered avg
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.

Time complexity: O(3N) 
(Details: one for min calc, one for max calc. and one for loop)
Space complexity: O(1)
"""
def centeredAvg(input):
    s = min(input)
    l = max(input)
    c, nums, igOS, igOL = 0, 0, 0, 0
    for x in input:                
        if (x == s and igOS == 0):            
            igOS = 1            
        elif (x == l and igOL == 0):                       
            igOL = 1
        else:
            c += x 
            nums = nums + 1 
    output = (c // nums)
    return output 
    
assert centeredAvg([1, 2, 3, 4, 100]) == 3
assert centeredAvg([1, 1, 5, 5, 10, 8, 7]) == 5
assert centeredAvg([-10, -4, -2, -4, -2, 0]) == -3