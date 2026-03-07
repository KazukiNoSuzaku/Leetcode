# You have a graph of n nodes. You are given an integer n and an array edges where
# edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1

# Constraints:
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

# Author: Kaustav Ghosh

class Solution(object):
    def countComponents(self, n, edges):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        components = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                components -= 1
        return components
