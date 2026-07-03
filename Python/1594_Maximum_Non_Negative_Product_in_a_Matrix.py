# Author: Kaustav Ghosh
# Problem: Maximum Non Negative Product in a Matrix
# Approach: Track both the max and min product reaching each cell (a negative can flip min into the best), then read the corner

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        hi = [[0] * n for _ in range(m)]
        lo = [[0] * n for _ in range(m)]
        hi[0][0] = lo[0][0] = grid[0][0]

        for j in range(1, n):
            hi[0][j] = lo[0][j] = hi[0][j - 1] * grid[0][j]
        for i in range(1, m):
            hi[i][0] = lo[i][0] = hi[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                g = grid[i][j]
                cands = [hi[i - 1][j] * g, lo[i - 1][j] * g,
                         hi[i][j - 1] * g, lo[i][j - 1] * g]
                hi[i][j] = max(cands)
                lo[i][j] = min(cands)

        best = hi[m - 1][n - 1]
        return best % MOD if best >= 0 else -1
