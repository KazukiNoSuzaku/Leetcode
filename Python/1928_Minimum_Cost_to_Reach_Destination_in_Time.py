# Author: Kaustav Ghosh
# Problem: Minimum Cost to Reach Destination in Time
# Approach: dp[t][city] = min total fee to be at city having spent exactly t time. Time only increases along edges, so sweep t from 0 to maxTime and relax every edge. The answer is the cheapest way to be at city n-1 at any time within maxTime

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = float('inf')
        dp = [[INF] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        for t in range(maxTime + 1):
            row = dp[t]
            for node in range(n):
                cur = row[node]
                if cur == INF:
                    continue
                for nbr, w in adj[node]:
                    nt = t + w
                    if nt <= maxTime and cur + passingFees[nbr] < dp[nt][nbr]:
                        dp[nt][nbr] = cur + passingFees[nbr]

        best = min(dp[t][n - 1] for t in range(maxTime + 1))
        return -1 if best == INF else best
