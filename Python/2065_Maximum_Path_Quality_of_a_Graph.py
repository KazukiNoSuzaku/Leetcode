# Author: Kaustav Ghosh
# Problem: Maximum Path Quality of a Graph
# Approach: Each edge costs at least 10 and maxTime is at most 100, so any path has at most 10 edges. DFS all walks from node 0 within the time budget, adding a node's value only the first time it is visited, and record the best quality whenever back at node 0

from collections import defaultdict

class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b, t in edges:
            graph[a].append((b, t))
            graph[b].append((a, t))

        visited = [0] * len(values)
        self.best = 0

        def dfs(node, time_left, quality):
            if node == 0:
                self.best = max(self.best, quality)
            for nei, cost in graph[node]:
                if cost <= time_left:
                    gain = values[nei] if visited[nei] == 0 else 0
                    visited[nei] += 1
                    dfs(nei, time_left - cost, quality + gain)
                    visited[nei] -= 1

        visited[0] = 1
        dfs(0, maxTime, values[0])
        return self.best
