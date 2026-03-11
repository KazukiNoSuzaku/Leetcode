# Given an m x n binary matrix mat, return the length of the longest line of consecutive
# 1s in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

# Author: Kaustav Ghosh

class Solution(object):
    def longestLine(self, mat):
        if not mat: return 0
        m, n = len(mat), len(mat[0])
        dp = [[[0]*4 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    dp[i][j][0] = (dp[i][j-1][0] if j > 0 else 0) + 1
                    dp[i][j][1] = (dp[i-1][j][1] if i > 0 else 0) + 1
                    dp[i][j][2] = (dp[i-1][j-1][2] if i > 0 and j > 0 else 0) + 1
                    dp[i][j][3] = (dp[i-1][j+1][3] if i > 0 and j < n-1 else 0) + 1
                    res = max(res, max(dp[i][j]))
        return res
