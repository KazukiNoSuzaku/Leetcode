# Author: Kaustav Ghosh
# Problem: Constrained Subsequence Sum
# Approach: Monotone deque max DP within window k

from collections import deque

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = nums[:]
        dq = deque()  # stores indices with decreasing dp values
        for i in range(n):
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
        return max(dp)
