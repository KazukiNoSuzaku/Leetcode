# Author: Kaustav Ghosh
# Problem: Min Cost to Connect All Points
# Approach: Prim's MST on the dense graph of Manhattan distances; repeatedly pull in the nearest outside point and relax the rest

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        in_mst = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for v in range(n):
                if not in_mst[v] and (u == -1 or dist[v] < dist[u]):
                    u = v
            in_mst[u] = True
            total += dist[u]
            ux, uy = points[u]
            for v in range(n):
                if not in_mst[v]:
                    d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
        return total
