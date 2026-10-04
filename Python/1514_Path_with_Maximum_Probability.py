# Author: Kaustav Ghosh
# Problem: Path with Maximum Probability
# Approach: Probabilities multiply and never exceed 1, so extending a path can only lower it, which is exactly the monotonicity Dijkstra needs. Run it with a max-heap on the running probability and stop as soon as the end node is settled

import heapq


class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = [[] for _ in range(n)]
        for (a, b), probability in zip(edges, succProb):
            graph[a].append((b, probability))
            graph[b].append((a, probability))
        best = [0.0] * n
        best[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            negated, node = heapq.heappop(heap)
            reached = -negated
            if node == end_node:
                return reached
            if reached < best[node]:
                continue
            for nxt, probability in graph[node]:
                candidate = reached * probability
                if candidate > best[nxt]:
                    best[nxt] = candidate
                    heapq.heappush(heap, (-candidate, nxt))
        return 0.0
