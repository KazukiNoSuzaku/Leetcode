# Author: Kaustav Ghosh
# 1102. Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/

import heapq

class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while heap:
            neg_val, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return -neg_val
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (max(neg_val, -grid[nr][nc]), nr, nc))
        return -1
