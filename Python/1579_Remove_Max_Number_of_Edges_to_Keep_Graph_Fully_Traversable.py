# Author: Kaustav Ghosh
# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable
# Approach: Union-Find per user; add shared (type-3) edges first, then each user's own edges, keeping only merging ones. Removable = total - kept

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        self.components -= 1
        return True


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        alice, bob = DSU(n), DSU(n)
        kept = 0

        for t, u, v in edges:
            if t == 3:
                merged = alice.union(u, v)
                bob.union(u, v)
                if merged:
                    kept += 1

        for t, u, v in edges:
            if t == 1 and alice.union(u, v):
                kept += 1
            elif t == 2 and bob.union(u, v):
                kept += 1

        if alice.components == 1 and bob.components == 1:
            return len(edges) - kept
        return -1
