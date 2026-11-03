# Author: Kaustav Ghosh
# Problem: Number of Restricted Paths From First to Last Node
# Approach: A restricted path must strictly decrease the shortest distance to node n at every step, so one Dijkstra run from node n gives every node its distance and, more usefully, orients each edge: it may only be walked from the higher distance to the lower. That orientation is acyclic, which turns path counting into a single pass over the nodes in increasing order of distance, each node summing the counts of the neighbours strictly closer to the end. Dijkstra already pops nodes in exactly that order, so the counting rides along on the same traversal.

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from heapq import heappop, heappush

        MOD = 10 ** 9 + 7
        adjacency = [[] for _ in range(n + 1)]
        for u, v, weight in edges:
            adjacency[u].append((v, weight))
            adjacency[v].append((u, weight))

        INF = float("inf")
        distance = [INF] * (n + 1)
        distance[n] = 0
        paths = [0] * (n + 1)
        paths[n] = 1
        settled = [False] * (n + 1)

        heap = [(0, n)]
        while heap:
            dist, node = heappop(heap)
            if settled[node]:
                continue
            settled[node] = True
            # Every neighbour already settled is strictly closer to node n,
            # so its path count is final and can be folded in here.
            total = 0
            for neighbour, weight in adjacency[node]:
                if settled[neighbour] and distance[neighbour] < dist:
                    total += paths[neighbour]
            if node != n:
                paths[node] = total % MOD
            for neighbour, weight in adjacency[node]:
                if dist + weight < distance[neighbour]:
                    distance[neighbour] = dist + weight
                    heappush(heap, (dist + weight, neighbour))
        return paths[1] % MOD
