# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Author: Kaustav Ghosh

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
