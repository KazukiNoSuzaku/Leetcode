# Author: Kaustav Ghosh
# Problem 1857: Largest Color Value in a Directed Graph

from collections import deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        # dp[node][color] = max count of that color on any path ending at node
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1
        visited = 0
        result = 0
        while queue:
            node = queue.popleft()
            visited += 1
            result = max(result, max(dp[node]))
            for nei in adj[node]:
                for c in range(26):
                    val = dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0)
                    if val > dp[nei][c]:
                        dp[nei][c] = val
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if visited != n:
            return -1
        return result
