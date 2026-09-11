# Author: Kaustav Ghosh
# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph
# Approach: Two nodes are unreachable from each other exactly when they lie in different connected components. Find component sizes with union-find; the number of cross-component pairs is the running total of (size of new component) times (nodes already counted)

class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]

        pairs = 0
        counted = 0
        seen_roots = set()
        for i in range(n):
            r = find(i)
            if r not in seen_roots:
                seen_roots.add(r)
                comp = size[r]
                pairs += comp * counted
                counted += comp
        return pairs
