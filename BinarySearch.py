"""
binary search- Write a function for binary search 
to determine whether a given number array has the target value. 
Time complexity: O(log n) for average/worst case, 
O(1) in best case (searching for the middle number)
"""
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target: return pivot
        if target < nums[pivot]: right = pivot - 1
        else: left = pivot + 1
                
    return -1
  
assert search([1, 2, 4, 6, 8, 10, 12, 14, 16], 6) == 3