# Author: Kaustav Ghosh
# Problem: Minimum Subarrays in a Valid Split
# Approach: Only where the cuts fall matters, so dp[end] is the fewest subarrays covering the first end elements. A subarray from start to end - 1 is allowed when its two ends share a factor, so extend every reachable prefix that way and report -1 when the whole array stays unreachable

from math import gcd


class Solution(object):
    def validSubarraySplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        INF = float('inf')
        dp = [0] + [INF] * n
        for end in range(1, n + 1):
            last = nums[end - 1]
            for start in range(end):
                if dp[start] + 1 < dp[end] and gcd(nums[start], last) > 1:
                    dp[end] = dp[start] + 1
        return -1 if dp[n] == INF else dp[n]
