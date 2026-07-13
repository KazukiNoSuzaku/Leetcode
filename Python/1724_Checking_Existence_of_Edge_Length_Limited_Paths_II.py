# Author: Kaustav Ghosh
# Problem: Checking Existence of Edge Length Limited Paths II (Premium)
# Approach: The minimum spanning forest also minimizes the bottleneck (max edge) on every path, so build it with Kruskal, then binary-lift each node storing the heaviest edge above it; a query is true iff that path maximum is below the limit

from collections import deque

class DistanceLimitedPathsExist(object):
    def __init__(self, n, edgeList):
        """
        :type n: int
        :type edgeList: List[List[int]]
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # Kruskal: keep only the minimum spanning forest edges
        adj = [[] for _ in range(n)]
        for u, v, w in sorted(edgeList, key=lambda e: e[2]):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                adj[u].append((v, w))
                adj[v].append((u, w))

        LOG = max(1, n.bit_length())
        self.LOG = LOG
        self.up = [[-1] * LOG for _ in range(n)]
        self.mx = [[0] * LOG for _ in range(n)]
        self.depth = [0] * n
        self.comp = [-1] * n

        seen = [False] * n
        for root in range(n):
            if seen[root]:
                continue
            seen[root] = True
            self.comp[root] = root
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v, w in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        self.comp[v] = root
                        self.depth[v] = self.depth[u] + 1
                        self.up[v][0] = u
                        self.mx[v][0] = w
                        queue.append(v)

        for j in range(1, LOG):
            for v in range(n):
                mid = self.up[v][j - 1]
                if mid != -1:
                    self.up[v][j] = self.up[mid][j - 1]
                    self.mx[v][j] = max(self.mx[v][j - 1], self.mx[mid][j - 1])

    def query(self, p, q, limit):
        """
        :type p: int
        :type q: int
        :type limit: int
        :rtype: bool
        """
        if self.comp[p] != self.comp[q]:
            return False

        heaviest = 0
        if self.depth[p] < self.depth[q]:
            p, q = q, p

        diff = self.depth[p] - self.depth[q]
        for j in range(self.LOG):
            if diff >> j & 1:
                heaviest = max(heaviest, self.mx[p][j])
                p = self.up[p][j]

        if p == q:
            return heaviest < limit

        for j in range(self.LOG - 1, -1, -1):
            if self.up[p][j] != self.up[q][j]:
                heaviest = max(heaviest, self.mx[p][j], self.mx[q][j])
                p = self.up[p][j]
                q = self.up[q][j]

        heaviest = max(heaviest, self.mx[p][0], self.mx[q][0])
        return heaviest < limit
