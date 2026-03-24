# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

import heapq
from collections import defaultdict

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Dijkstra with state (cost, time, node)
        # min_time[node] = minimum time to reach node
        min_time = [float('inf')] * n
        min_time[0] = 0
        pq = [(passingFees[0], 0, 0)]  # (cost, time, node)

        while pq:
            cost, time, node = heapq.heappop(pq)
            if node == n - 1:
                return cost
            if time > min_time[node]:
                continue
            for nei, t in graph[node]:
                new_time = time + t
                if new_time < min_time[nei] and new_time <= maxTime:
                    min_time[nei] = new_time
                    heapq.heappush(pq, (cost + passingFees[nei], new_time, nei))

        return -1
