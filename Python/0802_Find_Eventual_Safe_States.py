# Find all safe nodes (not part of or leading to a cycle) in a directed graph.

# Author: Kaustav Ghosh

class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n
        def dfs(node):
            if state[node]: return state[node] == 2
            state[node] = 1
            for nb in graph[node]:
                if not dfs(nb): return False
            state[node] = 2
            return True
        return [i for i in range(n) if dfs(i)]
