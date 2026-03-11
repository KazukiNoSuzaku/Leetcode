# Find shortest string containing all n-digit combinations with k digits (Eulerian path).

# Author: Kaustav Ghosh

class Solution(object):
    def crackSafe(self, n, k):
        start = '0' * (n - 1)
        visited = set()
        res = []
        def dfs(node):
            for d in map(str, range(k)):
                edge = node + d
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    res.append(d)
        dfs(start)
        return start + ''.join(reversed(res))
