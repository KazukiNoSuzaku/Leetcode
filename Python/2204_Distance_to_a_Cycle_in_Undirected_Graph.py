# Author: Kaustav Ghosh
# Problem: Distance to a Cycle in Undirected Graph
# Approach: The graph has n nodes and n edges, so it contains exactly one cycle. Repeatedly strip degree-1 leaves until only the cycle remains; those surviving nodes are the cycle. Then run a multi-source BFS from all cycle nodes to get every node's distance to the cycle

from collections import deque


class Solution(object):
    def distanceToCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [set() for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        # Peel leaves (degree 1) until only cycle nodes remain
        removed = [False] * n
        leaves = deque(i for i in range(n) if degree[i] == 1)
        while leaves:
            leaf = leaves.popleft()
            removed[leaf] = True
            for nb in adj[leaf]:
                if not removed[nb]:
                    degree[nb] -= 1
                    if degree[nb] == 1:
                        leaves.append(nb)

        # Multi-source BFS from all cycle nodes
        dist = [-1] * n
        q = deque()
        for i in range(n):
            if not removed[i]:
                dist[i] = 0
                q.append(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
