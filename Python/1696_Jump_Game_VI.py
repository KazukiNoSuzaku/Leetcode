# Author: Kaustav Ghosh
# https://leetcode.com/problems/jump-game-vi/

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
        dq = deque([0])
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = dp[dq[0]] + nums[i]
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        return dp[n - 1]
