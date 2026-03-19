# Author: Kaustav Ghosh
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
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

        edgeList.sort(key=lambda x: x[2])
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1][2])

        result = [False] * len(queries)
        ei = 0
        for qi, (p, q, limit) in indexed_queries:
            while ei < len(edgeList) and edgeList[ei][2] < limit:
                union(edgeList[ei][0], edgeList[ei][1])
                ei += 1
            result[qi] = find(p) == find(q)
        return result
