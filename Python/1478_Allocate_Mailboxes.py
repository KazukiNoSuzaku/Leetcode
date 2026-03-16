# Author: Kaustav Ghosh
# Problem: Allocate Mailboxes
# Approach: DP + median minimizes total distance for each group

class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        houses.sort()
        n = len(houses)

        # cost[i][j] = cost to serve houses[i..j] with one mailbox (at median)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                for h in range(i, j + 1):
                    cost[i][j] += abs(houses[h] - median)

        # dp[i][j] = min cost for first i houses with j mailboxes
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for start in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[start][j - 1] + cost[start][i - 1])
        return dp[n][k]
