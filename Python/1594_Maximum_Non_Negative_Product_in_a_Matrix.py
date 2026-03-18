# Author: Kaustav Ghosh
# Problem: 1594 - Maximum Non Negative Product in a Matrix
# Approach: DP tracking both max and min products at each cell

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for i in range(1, rows):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        for j in range(1, cols):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                candidates = [
                    max_dp[i-1][j] * grid[i][j],
                    min_dp[i-1][j] * grid[i][j],
                    max_dp[i][j-1] * grid[i][j],
                    min_dp[i][j-1] * grid[i][j]
                ]
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        if max_dp[rows-1][cols-1] < 0:
            return -1
        return max_dp[rows-1][cols-1] % MOD
