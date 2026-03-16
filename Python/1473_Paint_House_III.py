# Author: Kaustav Ghosh
# Problem: Paint House III
# Approach: 3D DP: house index, number of neighborhoods, last color

class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        INF = float('inf')
        # dp[i][j][c] = min cost to paint houses[0..i] with j neighborhoods, house i colored c
        dp = [[[INF] * (n + 1) for _ in range(target + 1)] for _ in range(m)]

        if houses[0] != 0:
            dp[0][1][houses[0]] = 0
        else:
            for c in range(1, n + 1):
                dp[0][1][c] = cost[0][c - 1]

        for i in range(1, m):
            for j in range(1, min(i + 2, target + 1)):
                if houses[i] != 0:
                    c = houses[i]
                    for pc in range(1, n + 1):
                        if pc == c:
                            dp[i][j][c] = min(dp[i][j][c], dp[i - 1][j][pc])
                        else:
                            if j > 1:
                                dp[i][j][c] = min(dp[i][j][c], dp[i - 1][j - 1][pc])
                else:
                    for c in range(1, n + 1):
                        paint = cost[i][c - 1]
                        for pc in range(1, n + 1):
                            if pc == c:
                                dp[i][j][c] = min(dp[i][j][c], dp[i - 1][j][pc] + paint)
                            else:
                                if j > 1:
                                    dp[i][j][c] = min(dp[i][j][c], dp[i - 1][j - 1][pc] + paint)

        result = min(dp[m - 1][target][c] for c in range(1, n + 1))
        return result if result < INF else -1
