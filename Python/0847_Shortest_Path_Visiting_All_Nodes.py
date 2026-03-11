# Find shortest path length visiting all nodes in an undirected graph.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        full = (1 << n) - 1
        q = deque([(i, 1 << i, 0) for i in range(n)])
        visited = set((i, 1 << i) for i in range(n))
        while q:
            node, state, steps = q.popleft()
            if state == full: return steps
            for nb in graph[node]:
                new_state = state | (1 << nb)
                if (nb, new_state) not in visited:
                    visited.add((nb, new_state))
                    q.append((nb, new_state, steps + 1))
        return -1
