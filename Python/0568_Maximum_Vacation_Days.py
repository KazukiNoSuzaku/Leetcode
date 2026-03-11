# LeetCode wants to give one of its best employees the option to travel among n cities to collect
# algorithm problems. Given flights (n x n adjacency matrix) and days (n x k vacation days),
# return the maximum vacation days you could take.

# Author: Kaustav Ghosh

class Solution(object):
    def maxVacationDays(self, flights, days):
        n, k = len(flights), len(days[0])
        INF = float('-inf')
        dp = [INF] * n
        dp[0] = 0
        for week in range(k):
            ndp = [INF] * n
            for to in range(n):
                for frm in range(n):
                    if (frm == to or flights[frm][to]) and dp[frm] != INF:
                        ndp[to] = max(ndp[to], dp[frm] + days[to][week])
            dp = ndp
        return max(dp)
