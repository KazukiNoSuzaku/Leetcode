# Author: Kaustav Ghosh
# Problem: Restore the Array From Adjacent Pairs
# Approach: The pairs form a path graph, so the two endpoints are the nodes with a single neighbor; start at one and walk across, never stepping back

from collections import defaultdict

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        start = next(node for node, nbrs in adj.items() if len(nbrs) == 1)

        n = len(adjacentPairs) + 1
        res = [start]
        prev, cur = None, start
        while len(res) < n:
            for nxt in adj[cur]:
                if nxt != prev:
                    res.append(nxt)
                    prev, cur = cur, nxt
                    break
        return res
