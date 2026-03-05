# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for n in nums:
            if n != 0:
                nums[pos] = n
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
