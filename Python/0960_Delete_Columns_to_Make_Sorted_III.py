# Given an array of strings strs, delete the minimum number of columns
# so that the remaining columns are non-decreasing per row as a sequence (LIS-style).

# Author: Kaustav Ghosh

class Solution(object):
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        dp = [1] * m
        for j in range(1, m):
            for i in range(j):
                if all(strs[r][i] <= strs[r][j] for r in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return m - max(dp)
