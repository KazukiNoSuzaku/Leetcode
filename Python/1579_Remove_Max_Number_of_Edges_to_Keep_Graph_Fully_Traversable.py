# Author: Kaustav Ghosh
# Problem: 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
# Approach: Union-Find: add type-3 edges first, then type-1 and type-2

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        class UF:
            def __init__(self, n):
                self.parent = list(range(n + 1))
                self.rank = [0] * (n + 1)
                self.components = n

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                self.components -= 1
                return True

        uf_alice = UF(n)
        uf_bob = UF(n)
        removed = 0

        # Add type 3 edges first
        for t, u, v in edges:
            if t == 3:
                a = uf_alice.union(u, v)
                b = uf_bob.union(u, v)
                if not a and not b:
                    removed += 1

        for t, u, v in edges:
            if t == 1:
                if not uf_alice.union(u, v):
                    removed += 1
            elif t == 2:
                if not uf_bob.union(u, v):
                    removed += 1

        if uf_alice.components == 1 and uf_bob.components == 1:
            return removed
        return -1
