# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, return an array of all the integers that appear twice.

# Author: Kaustav Ghosh

class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            else:
                nums[idx] = -nums[idx]
        return res
