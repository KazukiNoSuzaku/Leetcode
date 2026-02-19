# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
# such that each unique element appears at most twice. The relative order of the elements
# should be kept the same.

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# Author: Kaustav Ghosh

class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for num in nums:
            if k < 2 or nums[k - 2] != num:
                nums[k] = num
                k += 1
        return k
