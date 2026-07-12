# Author: Kaustav Ghosh
# Problem: Jump Game VI
# Approach: dp[i] = nums[i] + best dp within the previous k indices; a monotonic deque keeps that window maximum in O(1) amortized

from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        window = deque([0])  # indices, decreasing dp values

        for i in range(1, n):
            while window and window[0] < i - k:
                window.popleft()
            dp[i] = dp[window[0]] + nums[i]
            while window and dp[window[-1]] <= dp[i]:
                window.pop()
            window.append(i)
        return dp[n - 1]
