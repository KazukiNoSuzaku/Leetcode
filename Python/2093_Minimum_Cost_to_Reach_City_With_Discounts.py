# Author: Kaustav Ghosh
# Problem: Minimum Cost to Reach City With Discounts
# Approach: Dijkstra over states (city, discounts used). From a city, each highway can be taken at full toll or, if a discount remains, at half toll (floored) spending one discount. The answer is the cheapest way to reach the last city with any number of discounts used

import heapq

class Solution(object):
    def minimumCost(self, n, highways, discounts):
        """
        :type n: int
        :type highways: List[List[int]]
        :type discounts: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))

        INF = float('inf')
        dist = [[INF] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (cost, city, discounts_used)
        while heap:
            cost, u, d = heapq.heappop(heap)
            if cost > dist[u][d]:
                continue
            if u == n - 1:
                return cost
            for v, toll in graph[u]:
                if cost + toll < dist[v][d]:
                    dist[v][d] = cost + toll
                    heapq.heappush(heap, (cost + toll, v, d))
                if d < discounts and cost + toll // 2 < dist[v][d + 1]:
                    dist[v][d + 1] = cost + toll // 2
                    heapq.heappush(heap, (cost + toll // 2, v, d + 1))

        return -1
