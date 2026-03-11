# Count nodes reachable in a graph where edges are subdivided with extra nodes.

# Author: Kaustav Ghosh

import heapq
from collections import defaultdict

class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt
        dist = {0: maxMoves}
        heap = [(-maxMoves, 0)]
        res = 0
        while heap:
            d, u = heapq.heappop(heap)
            d = -d
            if d < dist.get(u, -1): continue
            res += 1
            for v, cnt in graph[u].items():
                if d - cnt - 1 >= 0 and v not in dist:
                    dist[v] = d - cnt - 1
                    heapq.heappush(heap, (-(d-cnt-1), v))
        for u, v, cnt in edges:
            res += min(cnt, dist.get(u, 0) + dist.get(v, 0))
        return res
