# Author: Kaustav Ghosh
# Problem: 1584 - Min Cost to Connect All Points
# Approach: Prim's MST on Manhattan distances

import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        total = 0
        count = 0

        while count < n:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total += cost
            count += 1
            for v in range(n):
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (d, v))

        return total
