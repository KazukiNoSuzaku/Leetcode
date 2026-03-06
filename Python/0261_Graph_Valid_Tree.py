# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of
# edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false

# Constraints:
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2

# Author: Kaustav Ghosh

class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True
