# Author: Kaustav Ghosh
# Problem: Maximum Non Negative Product in a Matrix
# Approach: Keeping only the best product per cell is not enough, because a negative cell turns the worst running product into the best one, so each cell carries both the largest and the smallest product reachable there; a new cell extends both candidates from above and from the left and the extremes are taken over all of them. The modulo is applied only to the final answer, never during the DP, since reducing intermediate products would destroy the sign and the ordering the DP depends on.

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        rows, cols = len(grid), len(grid[0])
        high = [[0] * cols for _ in range(rows)]
        low = [[0] * cols for _ in range(rows)]
        high[0][0] = low[0][0] = grid[0][0]

        for c in range(1, cols):
            high[0][c] = low[0][c] = high[0][c - 1] * grid[0][c]
        for r in range(1, rows):
            high[r][0] = low[r][0] = high[r - 1][0] * grid[r][0]

        for r in range(1, rows):
            for c in range(1, cols):
                value = grid[r][c]
                candidates = (high[r - 1][c] * value, low[r - 1][c] * value,
                              high[r][c - 1] * value, low[r][c - 1] * value)
                high[r][c] = max(candidates)
                low[r][c] = min(candidates)

        best = high[rows - 1][cols - 1]
        return -1 if best < 0 else best % MOD
