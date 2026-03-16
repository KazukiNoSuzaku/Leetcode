# Author: Kaustav Ghosh
# Problem: Max Dot Product of Two Subsequences
# Approach: DP similar to LCS tracking maximum dot product

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    max(dp[i - 1][j - 1], 0) + nums1[i - 1] * nums2[j - 1]
                )
        return dp[m][n]
