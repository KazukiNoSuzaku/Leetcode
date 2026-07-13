# Author: Kaustav Ghosh
# Problem: Number Of Ways To Reconstruct A Tree (Premium)
# Approach: In the pair graph an ancestor's degree dominates its descendant's. The root must touch everyone; each node's parent is its lowest-degree neighbor with degree >= its own, whose neighborhood must contain all of the node's other pairs. An equal-degree parent means the two can swap, giving multiple trees

from collections import defaultdict

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)

        n = len(adj)
        nodes = sorted(adj, key=lambda x: len(adj[x]), reverse=True)

        # The root has to be paired with every other node
        if len(adj[nodes[0]]) != n - 1:
            return 0

        multiple = False
        for node in nodes:
            degree = len(adj[node])
            parent = None
            best = float('inf')
            for nei in adj[node]:
                d = len(adj[nei])
                if d >= degree and d < best:
                    best = d
                    parent = nei
            if parent is None:
                continue  # this is the root

            if len(adj[parent]) == degree:
                multiple = True  # node and parent are interchangeable

            # Every other pair of node must also be a pair of its parent
            for nei in adj[node]:
                if nei != parent and nei not in adj[parent]:
                    return 0

        return 2 if multiple else 1
