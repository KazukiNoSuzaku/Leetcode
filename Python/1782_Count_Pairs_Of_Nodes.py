# Author: Kaustav Ghosh
# Problem: Count Pairs Of Nodes
# Approach: For a pair (a,b) the incident-edge count is deg[a]+deg[b] minus shared edges. Sort degrees to two-pointer count pairs with deg sum > query, then correct each pair that shares edges by its exact overlap

from collections import Counter

class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        degree = [0] * (n + 1)
        shared = Counter()
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            shared[(min(u, v), max(u, v))] += 1

        ordered = sorted(degree[1:])  # degrees of nodes 1..n

        res = []
        for q in queries:
            # count unordered pairs with degree sum strictly greater than q
            count = 0
            lo, hi = 0, n - 1
            while lo < hi:
                if ordered[lo] + ordered[hi] > q:
                    count += hi - lo
                    hi -= 1
                else:
                    lo += 1
            # fix pairs that share edges (their real incident count is lower)
            for (u, v), c in shared.items():
                total = degree[u] + degree[v]
                if total > q and total - c <= q:
                    count -= 1
            res.append(count)
        return res
