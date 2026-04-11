# Author: Kaustav Ghosh
# Problem: 2290. Minimum Obstacle Removal to Reach Corner
# URL: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
# Difficulty: Hard
#
# Approach:
# 0-1 BFS (deque-based). Moving to an empty cell costs 0 (add to front),
# moving to an obstacle costs 1 (add to back). Find shortest path from
# (0,0) to (m-1,n-1).

from collections import deque

class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0, 0)])
        while dq:
            d, r, c = dq.popleft()
            if d > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nd = d + grid[nr][nc]
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if grid[nr][nc] == 0:
                            dq.appendleft((nd, nr, nc))
                        else:
                            dq.append((nd, nr, nc))
        return dist[m - 1][n - 1]
