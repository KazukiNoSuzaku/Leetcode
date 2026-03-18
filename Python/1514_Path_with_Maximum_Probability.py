# Author: Kaustav Ghosh
# Problem: 1514 - Path with Maximum Probability
# Approach: Modified Dijkstra with max-heap on probability

import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = [0.0] * n
        prob[start] = 1.0
        heap = [(-1.0, start)]

        while heap:
            p, node = heapq.heappop(heap)
            p = -p
            if node == end:
                return p
            if p < prob[node]:
                continue
            for neighbor, edge_prob in graph[node]:
                new_prob = p * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
