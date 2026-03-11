# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence is arithmetic if it has at least 3 elements and the differences between
# consecutive elements are the same.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                res += dp[j][diff]
        return res
