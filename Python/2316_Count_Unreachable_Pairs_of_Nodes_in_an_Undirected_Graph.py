# Author: Kaustav Ghosh
# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# Union-Find: count pairs across disconnected components

class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        for u, v in edges:
            union(u, v)

        # Count component sizes
        from collections import Counter
        comp_sizes = Counter(find(i) for i in range(n))
        sizes = list(comp_sizes.values())

        # For each component, all nodes in other components form unreachable pairs
        result = 0
        remaining = n
        for size in sizes:
            remaining -= size
            result += size * remaining

        return result
