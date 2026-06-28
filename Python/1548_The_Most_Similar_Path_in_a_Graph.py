# Author: Kaustav Ghosh
# Problem: The Most Similar Path in a Graph (Premium)
# Approach: DP from the end of targetPath; dp[i][v] = min edit distance for a valid path starting at city v aligned to targetPath[i:], with parent pointers to rebuild the path

class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        m = len(targetPath)
        INF = float('inf')
        dp = [[INF] * n for _ in range(m)]
        nxt = [[-1] * n for _ in range(m)]

        # base case: last position contributes 0 or 1 depending on a name match
        for v in range(n):
            dp[m - 1][v] = 0 if names[v] == targetPath[m - 1] else 1

        for i in range(m - 2, -1, -1):
            for v in range(n):
                cost = 0 if names[v] == targetPath[i] else 1
                for w in adj[v]:
                    if dp[i + 1][w] + cost < dp[i][v]:
                        dp[i][v] = dp[i + 1][w] + cost
                        nxt[i][v] = w

        start = min(range(n), key=lambda v: dp[0][v])
        path = [start]
        for i in range(m - 1):
            start = nxt[i][start]
            path.append(start)
        return path
