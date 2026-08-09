# Author: Kaustav Ghosh
# Problem: Find if Path Exists in Graph
# Approach: Union-find over the edges; source and destination are connected iff they share a root after all unions

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        return find(source) == find(destination)
