# Find time for all nodes to receive signal from source k using Dijkstra.

# Author: Kaustav Ghosh

import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {k: 0}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist.get(u, float('inf')): continue
            for v, w in graph[u]:
                if dist.get(v, float('inf')) > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        return max(dist.values()) if len(dist) == n else -1
