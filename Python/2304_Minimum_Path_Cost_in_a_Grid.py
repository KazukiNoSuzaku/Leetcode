# Author: Kaustav Ghosh
class Solution(object):
    def minPathCost(self, grid, moveCost):
        # type: (List[List[int]], List[List[int]]) -> int
        m, n = len(grid), len(grid[0])
        dp = list(grid[0])
        for i in range(1, m):
            new_dp = [float('inf')] * n
            for j in range(n):
                for k in range(n):
                    cost = dp[k] + moveCost[grid[i - 1][k]][j] + grid[i][j]
                    if cost < new_dp[j]:
                        new_dp[j] = cost
            dp = new_dp
        return min(dp)
