# Author: Kaustav Ghosh
# Problem 2088: Count Fertile Pyramids in a Land

class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count(grid):
            m, n = len(grid), len(grid[0])
            dp = [row[:] for row in grid]
            result = 0
            for i in range(1, m):
                for j in range(n):
                    if grid[i][j] == 1 and j > 0 and j < n - 1:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + 1
                    else:
                        dp[i][j] = grid[i][j]
                    if dp[i][j] > 1:
                        result += dp[i][j] - 1
            return result

        # Count pyramids (top to bottom) and inverse pyramids (bottom to top)
        total = count(grid)
        grid.reverse()
        total += count(grid)
        return total
