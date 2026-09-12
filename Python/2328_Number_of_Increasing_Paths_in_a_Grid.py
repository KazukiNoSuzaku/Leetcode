# Author: Kaustav Ghosh
# Problem: Number of Increasing Paths in a Grid
# Approach: For each cell, the number of strictly increasing paths starting there is 1 (itself) plus the sum over strictly-greater neighbors of their path counts. Memoize this (it is acyclic because values strictly increase along any path) and sum over all cells, modulo 1e9+7

import sys


class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]
        sys.setrecursionlimit(10 ** 6)

        def paths(r, c):
            if memo[r][c]:
                return memo[r][c]
            total = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    total += paths(nr, nc)
            memo[r][c] = total % MOD
            return memo[r][c]

        result = 0
        for r in range(m):
            for c in range(n):
                result += paths(r, c)
        return result % MOD
