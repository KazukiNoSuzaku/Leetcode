# Author: Kaustav Ghosh

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = set()
        degree = [0] * (n + 1)
        for u, v in edges:
            adj.add((min(u, v), max(u, v)))
            degree[u] += 1
            degree[v] += 1
        res = float('inf')
        for u, v in edges:
            for w in range(1, n + 1):
                a, b, c = u, v, w
                if (min(a, c), max(a, c)) in adj and (min(b, c), max(b, c)) in adj:
                    res = min(res, degree[a] + degree[b] + degree[c] - 6)
        return res if res != float('inf') else -1
