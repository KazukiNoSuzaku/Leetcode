# Author: Kaustav Ghosh
# Problem: 1548 - The Most Similar Path in a Graph (Premium)
# Approach: DP on graph paths matching target city names

class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)
        INF = float('inf')
        # dp[i][v] = min edit distance when at city v at step i
        dp = [[INF] * n for _ in range(m)]
        parent = [[-1] * n for _ in range(m)]

        for v in range(n):
            dp[0][v] = 0 if names[v] == targetPath[0] else 1

        for i in range(1, m):
            for v in range(n):
                cost = 0 if names[v] == targetPath[i] else 1
                for u in graph[v]:
                    if dp[i-1][u] + cost < dp[i][v]:
                        dp[i][v] = dp[i-1][u] + cost
                        parent[i][v] = u

        # Find best ending city
        last = min(range(n), key=lambda v: dp[m-1][v])
        path = []
        cur = last
        for i in range(m-1, -1, -1):
            path.append(cur)
            cur = parent[i][cur]
        return path[::-1]
