# Find the minimum time to swim from top-left to bottom-right in a rising water grid.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1: return t
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1
