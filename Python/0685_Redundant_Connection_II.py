# Find the redundant directed edge in a rooted tree with one extra edge.

# Author: Kaustav Ghosh

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        parent = list(range(len(edges) + 1))
        cand1 = cand2 = None
        for u, v in edges:
            if parent[v] != v:
                cand1 = [parent[v], v]
                cand2 = [u, v]
            else:
                parent[v] = u
        parent = list(range(len(edges) + 1))
        for u, v in edges:
            if cand2 and [u, v] == cand2: continue
            pu = self._find(parent, u)
            if pu == v: return cand1 if cand1 else [u, v]
            parent[v] = pu
        return cand2

    def _find(self, parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
