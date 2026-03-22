# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)

        nodes = list(adj.keys())
        n = len(nodes)

        # Root must be connected to all other nodes
        root = None
        for node in nodes:
            if len(adj[node]) == n - 1:
                root = node
                break
        if root is None:
            return 0

        has_multiple = False

        # Sort nodes by degree descending
        nodes.sort(key=lambda x: len(adj[x]), reverse=True)

        # For each node, find its parent: the node with smallest degree >= current degree
        # that is in its adjacency set
        parent = {}
        for i, node in enumerate(nodes):
            if node == root:
                parent[node] = -1
                continue
            # Find parent: first node before it in sorted order that is adjacent
            par = None
            for j in range(i - 1, -1, -1):
                if nodes[j] in adj[node]:
                    par = nodes[j]
                    break
            if par is None:
                return 0
            parent[node] = par
            # Check: all neighbors of node must be neighbors of parent (or parent itself)
            if not (adj[node] <= (adj[par] | {par})):
                return 0
            if len(adj[node]) == len(adj[par]):
                has_multiple = True

        return 2 if has_multiple else 1
