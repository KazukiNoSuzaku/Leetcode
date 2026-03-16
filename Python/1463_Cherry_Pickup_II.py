# Author: Kaustav Ghosh
# Problem: Cherry Pickup II
# Approach: DP two robots moving down grid simultaneously

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        result = 0
        for r in range(1, m):
            for c1 in range(min(r + 1, n)):
                for c2 in range(max(0, n - 1 - r), n):
                    best = -1
                    for dc1 in [-1, 0, 1]:
                        for dc2 in [-1, 0, 1]:
                            pc1, pc2 = c1 - dc1, c2 - dc2
                            if 0 <= pc1 < n and 0 <= pc2 < n and dp[r - 1][pc1][pc2] >= 0:
                                best = max(best, dp[r - 1][pc1][pc2])
                    if best >= 0:
                        cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
                        dp[r][c1][c2] = best + cherries
                        if r == m - 1:
                            result = max(result, dp[r][c1][c2])

        if m == 1:
            return dp[0][0][n - 1]
        return result
