# Author: Kaustav Ghosh
# Problem: 2328. Number of Increasing Paths in a Grid
# URL: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Difficulty: Hard
#
# Approach:
# For each cell, use DFS with memoization to count increasing paths starting from that cell.
# A path is strictly increasing, so we only move to neighbors with strictly greater values.
# Sum dp[r][c] for all cells.

class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            count = 1  # path of length 1 (just this cell)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    count = (count + dfs(nr, nc)) % MOD
            memo[(r, c)] = count
            return count

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = (ans + dfs(r, c)) % MOD
        return ans
