# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-'
# before each integer in nums and then concatenate all the integers.
# Return the number of different expressions that you can build which evaluates to target.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            new_dp = defaultdict(int)
            for s, count in dp.items():
                new_dp[s + n] += count
                new_dp[s - n] += count
            dp = new_dp
        return dp[target]
