"""
Common numbers in two number lists 
Find the common numbers in two number arrays
Time complexity: 
O(min(N or M)) - Average cases
O(N*M) - Worst case

Space complexity:O(N+M) for the two sets
N is number of elements in set of nums1
M is number of elements in set of nums2
"""
def commonNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

assert common([1, 2,5,5,-1,25,0,.5,None], [2, 5]) == [2,5]
