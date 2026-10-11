# Author: Kaustav Ghosh
# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable
# Approach: Removing the most edges means keeping the fewest, so I build a minimal edge set with two union-find structures, one per traveller. A shared edge helps both at once, so every shared edge that joins two components is strictly better than any pair of single-type edges doing the same job and is therefore taken first; afterwards each traveller's own edges only fill in whatever gaps remain in that traveller's forest. An edge is kept exactly when it merges two components for someone, and if either forest ends up as more than one component the graph cannot be made fully traversable.

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        class Forest(object):
            def __init__(self, size):
                self.parent = list(range(size + 1))
                self.components = size

            def find(self, x):
                root = x
                while self.parent[root] != root:
                    root = self.parent[root]
                while self.parent[x] != root:
                    self.parent[x], x = root, self.parent[x]
                return root

            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False
                self.parent[ra] = rb
                self.components -= 1
                return True

        alice, bob = Forest(n), Forest(n)
        kept = 0
        for kind, u, v in edges:
            if kind == 3:
                merged_alice = alice.union(u, v)
                merged_bob = bob.union(u, v)
                if merged_alice or merged_bob:
                    kept += 1
        for kind, u, v in edges:
            if kind == 1 and alice.union(u, v):
                kept += 1
            elif kind == 2 and bob.union(u, v):
                kept += 1

        if alice.components != 1 or bob.components != 1:
            return -1
        return len(edges) - kept
