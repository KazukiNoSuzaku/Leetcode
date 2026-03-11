# Find and return the edge that creates a cycle in an undirected graph (tree + 1 edge).

# Author: Kaustav Ghosh

class Solution(object):
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]
            parent[pu] = pv
        return []
