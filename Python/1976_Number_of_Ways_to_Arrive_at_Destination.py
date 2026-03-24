# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

import heapq
from collections import defaultdict

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, t in graph[u]:
                if d + t < dist[v]:
                    dist[v] = d + t
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                elif d + t == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]
