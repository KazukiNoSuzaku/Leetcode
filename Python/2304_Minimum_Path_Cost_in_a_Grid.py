# Author: Kaustav Ghosh
# Problem: Minimum Path Cost in a Grid
# Approach: DP row by row. dp[c] is the minimum cost to reach cell (row, c). Moving to a cell in the next row costs that cell's value plus moveCost indexed by the current cell's value and the target column. Take the minimum over all previous columns; the answer is the smallest dp value in the last row

class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = list(grid[0])
        for r in range(1, m):
            ndp = [float('inf')] * n
            for nc in range(n):
                best = min(dp[c] + moveCost[grid[r - 1][c]][nc] for c in range(n))
                ndp[nc] = best + grid[r][nc]
            dp = ndp
        return min(dp)
