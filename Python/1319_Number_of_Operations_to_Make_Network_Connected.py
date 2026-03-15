# Find the minimum number of cable operations to connect all computers.
# Need at least n-1 edges and enough spare cables (edges > n-1).

# Author: Kaustav Ghosh

class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for u, v in connections:
            union(u, v)
        components = len(set(find(i) for i in range(n)))
        return components - 1
