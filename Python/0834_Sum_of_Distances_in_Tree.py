# Find sum of distances from each node to all other nodes in a tree.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v); graph[v].add(u)
        count = [1] * n
        res = [0] * n
        def dfs(node, parent):
            for nb in graph[node]:
                if nb != parent:
                    dfs(nb, node)
                    count[node] += count[nb]
                    res[node] += res[nb] + count[nb]
        def dfs2(node, parent):
            for nb in graph[node]:
                if nb != parent:
                    res[nb] = res[node] - count[nb] + (n - count[nb])
                    dfs2(nb, node)
        dfs(0, -1)
        dfs2(0, -1)
        return res
