# Author: Kaustav Ghosh
# Tarjan's algorithm for finding bridges in undirected graph

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [0] * n
        low = [0] * n
        visited = [False] * n
        bridges = []
        self.timer = 1

        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = self.timer
            self.timer += 1
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return bridges
