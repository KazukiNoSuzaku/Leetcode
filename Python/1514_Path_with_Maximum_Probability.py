# Author: Kaustav Ghosh
# Problem: Path with Maximum Probability
# Approach: Dijkstra with max-heap on probability; multiply edge probabilities along the path

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

        probs = [0.0] * n
        probs[start] = 1.0
        heap = [(-1.0, start)]

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob
            if node == end:
                return prob
            if prob < probs[node]:
                continue
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
