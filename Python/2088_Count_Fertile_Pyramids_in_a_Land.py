# Author: Kaustav Ghosh
# Problem: Count Fertile Pyramids in a Land
# Approach: For pyramids, dp[i][j] is the tallest pyramid with apex at (i,j): 1 + min of the three cells below (below-left, below, below-right) when fertile. Each cell contributes dp-1 pyramids of height >= 2. Inverse pyramids use the same DP scanning upward

class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def count(rows):
            # rows is the grid oriented so pyramids point downward from apex at smaller index
            dp = [[0] * n for _ in range(m)]
            total = 0
            for i in range(m - 1, -1, -1):
                for j in range(n):
                    if rows[i][j] == 0:
                        dp[i][j] = 0
                    elif i == m - 1 or j == 0 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1])
                    if dp[i][j] >= 2:
                        total += dp[i][j] - 1
            return total

        pyramids = count(grid)
        inverted = count(grid[::-1])
        return pyramids + inverted
