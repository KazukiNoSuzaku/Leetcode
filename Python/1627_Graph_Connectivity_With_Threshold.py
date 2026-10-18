# Author: Kaustav Ghosh
# Problem: Graph Connectivity With Threshold
# Approach: Two cities are joined when they share a divisor above the threshold, and rather than testing divisors for every pair I work from the divisors outward: for each candidate divisor above the threshold, all of its multiples share it and so belong to one component, which is achieved by uniting each multiple with the divisor itself. That costs n over d unions per divisor, and summing over the divisors is the harmonic series, so the whole structure is built in near-linear time instead of the quadratic cost of examining every pair. Each query is then a single comparison of the two cities' component roots.

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
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        for divisor in range(threshold + 1, n + 1):
            for multiple in range(divisor * 2, n + 1, divisor):
                a, b = find(divisor), find(multiple)
                if a != b:
                    parent[a] = b

        return [find(x) == find(y) for x, y in queries]
