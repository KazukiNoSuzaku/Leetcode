# Given an integer array nums, return true if you can partition the array into two subsets
# such that the sum of the elements in both subsets is equal or false otherwise.

# Author: Kaustav Ghosh

class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp = dp | {s + n for s in dp if s + n <= target}
        return target in dp
