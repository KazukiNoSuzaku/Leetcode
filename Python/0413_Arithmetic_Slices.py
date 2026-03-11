# An integer array is called arithmetic if it consists of at least three elements and
# if the difference between any two consecutive elements is the same.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# Author: Kaustav Ghosh

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        count = res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
                res += count
            else:
                count = 0
        return res
