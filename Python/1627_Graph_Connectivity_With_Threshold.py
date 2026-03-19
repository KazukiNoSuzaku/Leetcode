# Author: Kaustav Ghosh
# https://leetcode.com/problems/graph-connectivity-with-threshold/

class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

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

        for z in range(threshold + 1, n + 1):
            for multiple in range(2 * z, n + 1, z):
                union(z, multiple)

        return [find(a) == find(b) for a, b in queries]
