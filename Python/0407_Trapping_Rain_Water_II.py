# Given an m x n integer matrix heightMap representing the height of each unit cell,
# return the volume of water it can trap after raining.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    res += max(0, h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))
        return res
