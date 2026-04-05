# Author: Kaustav Ghosh
# 2203. Minimum Weighted Subgraph With the Required Paths
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
# Difficulty: Hard
#
# Approach: Run Dijkstra three times:
#   1. From src1 (forward edges)
#   2. From src2 (forward edges)
#   3. From dest (reversed edges)
# For each node v, the cost of routing both src1->dest and src2->dest through v is:
#   dist1[v] + dist2[v] + dist_dest[v]
# Take the minimum over all nodes v.

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
        INF = float('inf')

        # Build adjacency lists
        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        def dijkstra(start, adj):
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
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

        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        dist_dest = dijkstra(dest, rev_graph)

        ans = INF
        for v in range(n):
            ans = min(ans, dist1[v] + dist2[v] + dist_dest[v])

        return ans if ans < INF else -1
