# Author: Kaustav Ghosh
# Problem: Minimum Weighted Subgraph With the Required Paths
# Approach: Any valid subgraph is two paths src1->meet and src2->meet joining, then meet->dest, so the optimum is over a meeting node. Run Dijkstra from src1 and from src2 on the forward graph, and from dest on the reversed graph. The answer is the minimum over all nodes v of dist1[v] + dist2[v] + distDest[v]

import heapq


class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        forward = [[] for _ in range(n)]
        backward = [[] for _ in range(n)]
        for u, v, w in edges:
            forward[u].append((v, w))
            backward[v].append((u, w))

        def dijkstra(start, graph):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        d1 = dijkstra(src1, forward)
        d2 = dijkstra(src2, forward)
        d3 = dijkstra(dest, backward)

        best = min(d1[v] + d2[v] + d3[v] for v in range(n))
        return best if best != float('inf') else -1
