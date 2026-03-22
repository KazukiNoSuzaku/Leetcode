# Author: Kaustav Ghosh

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import heapq
        from collections import defaultdict
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        # DP: count paths where dist strictly decreases
        memo = {}
        def dp(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]
            count = 0
            for v, w in graph[node]:
                if dist[v] < dist[node]:
                    count = (count + dp(v)) % MOD
            memo[node] = count
            return count
        return dp(1)
