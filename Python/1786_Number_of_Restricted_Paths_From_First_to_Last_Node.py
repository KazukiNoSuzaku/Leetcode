# Author: Kaustav Ghosh
# Problem: Number of Restricted Paths From First to Last Node
# Approach: Dijkstra distances from node n, then count paths that strictly decrease in distance. Processing nodes in increasing distance lets a memoized DP accumulate path counts from n outward

import heapq
from collections import defaultdict

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nxt, w in adj[node]:
                if d + w < dist[nxt]:
                    dist[nxt] = d + w
                    heapq.heappush(pq, (dist[nxt], nxt))

        # ways[node] = number of restricted paths from node to n
        ways = [0] * (n + 1)
        ways[n] = 1
        for _, node in sorted((dist[i], i) for i in range(1, n + 1)):
            for nxt, _ in adj[node]:
                if dist[nxt] < dist[node]:  # must strictly decrease toward n
                    ways[node] = (ways[node] + ways[nxt]) % MOD
        return ways[1]
