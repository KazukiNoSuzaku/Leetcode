# Author: Kaustav Ghosh
# Problem: Checking Existence of Edge Length Limited Paths
# Approach: Answer queries offline sorted by limit; sweep edges (sorted by weight) into a union-find as their weight drops below the limit, then a query is true iff its endpoints share a root

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        edgeList.sort(key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i][2])

        res = [False] * len(queries)
        ei = 0
        for qi in order:
            p, q, limit = queries[qi]
            while ei < len(edgeList) and edgeList[ei][2] < limit:
                union(edgeList[ei][0], edgeList[ei][1])
                ei += 1
            res[qi] = find(p) == find(q)
        return res
