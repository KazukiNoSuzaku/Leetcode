# Given an integer array nums, add any number of parentheses to maximize the result.
# Return the corresponding expression in string format.

# Author: Kaustav Ghosh

class Solution(object):
    def optimalDivision(self, nums):
        if len(nums) == 1: return str(nums[0])
        if len(nums) == 2: return '%d/%d' % (nums[0], nums[1])
        return '%d/(%s)' % (nums[0], '/'.join(map(str, nums[1:])))
