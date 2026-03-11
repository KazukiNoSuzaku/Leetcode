# Determine if a graph is bipartite using BFS coloring.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node in color: continue
            q = deque([node])
            color[node] = 0
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v in color:
                        if color[v] == color[u]: return False
                    else:
                        color[v] = 1 - color[u]
                        q.append(v)
        return True
