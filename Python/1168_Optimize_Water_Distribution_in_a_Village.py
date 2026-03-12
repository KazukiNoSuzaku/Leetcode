# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Add virtual node 0 with well costs as edges, then Kruskal's MST

class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        edges = []
        for i, w in enumerate(wells):
            edges.append((w, 0, i + 1))
        for u, v, w in pipes:
            edges.append((w, u, v))
        edges.sort()

        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        total = 0
        for w, u, v in edges:
            if union(u, v):
                total += w
        return total
