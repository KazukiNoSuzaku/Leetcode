# A wiggle sequence is a sequence where the differences between successive numbers
# strictly alternate between positive and negative. The first difference (if one exists)
# may be either positive or negative. A sequence with one element and a sequence with
# two non-equal elements are trivially wiggle sequences.
# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

# Example 1:
# Input: nums = [1,7,4,9,2,5]
# Output: 6

# Example 2:
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def wiggleMaxLength(self, nums):
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
