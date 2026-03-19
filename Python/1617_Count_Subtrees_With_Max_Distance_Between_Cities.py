# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        def bfs(node, subset):
            dist = {node: 0}
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for nxt in adj[curr]:
                    if nxt in subset and nxt not in dist:
                        dist[nxt] = dist[curr] + 1
                        queue.append(nxt)
            return dist

        result = [0] * (n - 1)
        for mask in range(1, 1 << n):
            subset = set()
            for i in range(n):
                if mask & (1 << i):
                    subset.add(i)
            if len(subset) <= 1:
                continue
            start = next(iter(subset))
            dist = bfs(start, subset)
            if len(dist) != len(subset):
                continue
            farthest = max(dist, key=dist.get)
            dist2 = bfs(farthest, subset)
            diameter = max(dist2.values())
            if diameter > 0:
                result[diameter - 1] += 1

        return result
