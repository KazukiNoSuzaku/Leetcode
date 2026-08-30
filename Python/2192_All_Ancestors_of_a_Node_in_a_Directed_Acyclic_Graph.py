# Author: Kaustav Ghosh
# Problem: All Ancestors of a Node in a Directed Acyclic Graph
# Approach: Starting from each node in increasing order, DFS over the outgoing edges and record that node as an ancestor of every node it can reach. Visiting sources in increasing order means each ancestor list is built already sorted

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        ancestors = [[] for _ in range(n)]
        for src in range(n):
            visited = [False] * n
            stack = [src]
            visited[src] = True
            while stack:
                node = stack.pop()
                for nxt in adj[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        ancestors[nxt].append(src)
                        stack.append(nxt)
        return ancestors
