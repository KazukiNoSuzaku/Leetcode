import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, roads: list[list[int]], appleCost: list[int]) -> list[int]:
        adj = defaultdict(list)
        for a, b, c in roads:
            adj[a].append((b, c))
            adj[b].append((a, c))

        # Multi-source Dijkstra: each city starts with its apple purchase cost.
        # Propagating through roads finds the min total cost (travel + buy) for each city.
        dist = list(appleCost)
        heap = [(cost, i) for i, cost in enumerate(appleCost)]
        heapq.heapify(heap)

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        return dist
