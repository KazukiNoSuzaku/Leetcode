# Author: Kaustav Ghosh
# Problem: Largest Color Value in a Directed Graph
# Approach: Kahn topological order carrying, per node, the best count of each color on any path ending there. Add the node's own color when it is finalized, propagate maxima forward; if not all nodes are ordered there is a cycle

from collections import defaultdict, deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        adj = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue = deque(i for i in range(n) if indegree[i] == 0)

        seen = 0
        best = 0
        while queue:
            node = queue.popleft()
            seen += 1
            c = ord(colors[node]) - 97
            dp[node][c] += 1
            best = max(best, dp[node][c])
            for nxt in adj[node]:
                for color in range(26):
                    if dp[node][color] > dp[nxt][color]:
                        dp[nxt][color] = dp[node][color]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return best if seen == n else -1
