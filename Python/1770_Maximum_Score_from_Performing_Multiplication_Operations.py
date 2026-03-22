# Author: Kaustav Ghosh

class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        n = len(nums)
        # dp[i][j] = max score using i from left, j from right (i+j ops done)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for k in range(m - 1, -1, -1):
            for i in range(k, -1, -1):
                j = k - i
                pick_left = multipliers[k] * nums[i] + dp[i + 1][j]
                pick_right = multipliers[k] * nums[n - 1 - j] + dp[i][j + 1]
                dp[i][j] = max(pick_left, pick_right)
        return dp[0][0]
