
"""
Write a function to move Zeros of the given number array
Time complexity: O(2n)  ~ O(n)
Space complexity: O(1) 
"""
def moveZeros(nums):
    j = 0
    for num in nums:
        if(num != 0):
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0
    
    return nums

assert moveZeros([1, 0, 2, 3, 0, 0]) == [1, 2, 3, 0, 0, 0]