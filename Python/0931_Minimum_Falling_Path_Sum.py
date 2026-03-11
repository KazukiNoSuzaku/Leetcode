# Find minimum sum of a falling path through a matrix (adjacent columns allowed).

# Author: Kaustav Ghosh

class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = matrix[0][:]
        for r in range(1, n):
            new_dp = [0] * n
            for c in range(n):
                best = dp[c]
                if c > 0: best = min(best, dp[c-1])
                if c < n-1: best = min(best, dp[c+1])
                new_dp[c] = matrix[r][c] + best
            dp = new_dp
        return min(dp)
