import heapq
from collections import defaultdict

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.adj = defaultdict(list)
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = {node1: 0}
        heap = [(0, node1)]
        while heap:
            d, u = heapq.heappop(heap)
            if u == node2:
                return d
            if d > dist.get(u, float('inf')):
                continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return -1
