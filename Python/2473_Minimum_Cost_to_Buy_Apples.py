# Author: Kaustav Ghosh
# Problem: Minimum Cost to Buy Apples
# Approach: Starting at city i and buying at city j costs appleCost[j] plus the trip out and the trip home, which is (1 + k) times the shortest distance. Scaling every road by 1 + k and seeding each city with its own apple cost turns the whole thing into one multi-source Dijkstra: the settled distance of city i is its answer

import heapq


class Solution(object):
    def minCost(self, n, roads, appleCost, k):
        """
        :type n: int
        :type roads: List[List[int]]
        :type appleCost: List[int]
        :type k: int
        :rtype: List[int]
        """
        graph = [[] for _ in range(n + 1)]
        for a, b, cost in roads:
            graph[a].append((b, cost * (k + 1)))
            graph[b].append((a, cost * (k + 1)))
        best = [float('inf')] * (n + 1)
        heap = []
        for city in range(1, n + 1):
            best[city] = appleCost[city - 1]
            heap.append((best[city], city))
        heapq.heapify(heap)
        while heap:
            spent, city = heapq.heappop(heap)
            if spent > best[city]:
                continue
            for nxt, weight in graph[city]:
                if spent + weight < best[nxt]:
                    best[nxt] = spent + weight
                    heapq.heappush(heap, (best[nxt], nxt))
        return best[1:]
