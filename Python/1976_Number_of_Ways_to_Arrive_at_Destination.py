# Author: Kaustav Ghosh
# Problem: Number of Ways to Arrive at Destination
# Approach: Dijkstra from node 0, carrying a count of shortest paths per node. When a strictly shorter distance is found, reset the count; when an equal distance is found, add the predecessor's count

import heapq

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, t in graph[u]:
                nd = d + t
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(heap, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1] % MOD
