# Author: Kaustav Ghosh
# Problem: Graph Connectivity With Threshold
# Approach: For every divisor z > threshold, union it with all its multiples (they share z); then each query is a same-root check

class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for z in range(threshold + 1, n + 1):
            for multiple in range(2 * z, n + 1, z):
                union(z, multiple)

        return [find(a) == find(b) for a, b in queries]
