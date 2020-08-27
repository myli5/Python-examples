
"""
Two sum - Determine whether sum of two elements
give the target number in the list.
- return the two elements index if found
Time complexity: O(n)
Space complexity: O(2*n) ~ O(n) Dictionary 
"""
def twoSum(nums, target):
        m = {}
        n = len(nums)
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i
            
assert twoSum([10, 20, 40, 25, 85, 38], 48) == [0,5]