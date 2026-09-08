# Author: Kaustav Ghosh
# Problem: Closest Node to Path in Tree
# Approach: Precompute all-pairs distances with a BFS from every node (n is small). For each query, reconstruct the unique start-to-end path via a parent BFS, then pick the path node with the smallest precomputed distance to the query node

from collections import deque


class Solution(object):
    def closestNode(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # all-pairs distances via BFS from each node
        dist = [[-1] * n for _ in range(n)]
        for src in range(n):
            d = dist[src]
            d[src] = 0
            q = deque([src])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if d[w] == -1:
                        d[w] = d[u] + 1
                        q.append(w)

        def path(start, end):
            parent = [-1] * n
            seen = [False] * n
            seen[start] = True
            q = deque([start])
            while q:
                u = q.popleft()
                if u == end:
                    break
                for w in adj[u]:
                    if not seen[w]:
                        seen[w] = True
                        parent[w] = u
                        q.append(w)
            p = []
            cur = end
            while cur != -1:
                p.append(cur)
                cur = parent[cur]
            return p

        res = []
        for start, end, node in query:
            best_node = start
            best_d = dist[node][start]
            for p in path(start, end):
                if dist[node][p] < best_d:
                    best_d = dist[node][p]
                    best_node = p
            res.append(best_node)
        return res
