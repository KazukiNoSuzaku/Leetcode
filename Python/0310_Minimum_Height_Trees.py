# A tree is an undirected graph in which any two vertices are connected by exactly one path.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
# edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes,
# you can choose any node of the tree as the root. Return a list of all MHTs' root labels.
# The answer can be returned in any order.

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]

# Example 2:
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Constraints:
# 1 <= n <= 2 * 10^4
# edges.length == n - 1

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaves = deque(node for node in range(n) if len(adj[node]) == 1)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                nb = adj[leaf].pop()
                adj[nb].remove(leaf)
                if len(adj[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves
        return list(leaves)
