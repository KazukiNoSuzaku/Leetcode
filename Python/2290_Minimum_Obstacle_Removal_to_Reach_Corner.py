# Author: Kaustav Ghosh
# Problem: Minimum Obstacle Removal to Reach Corner
# Approach: Moving into a cell costs 1 if it holds an obstacle and 0 otherwise, so this is a shortest-path problem with edge weights 0/1. Run a 0-1 BFS with a deque: push zero-cost moves to the front and unit-cost moves to the back, giving the minimum obstacles to remove reaching the bottom-right

from collections import deque


class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nd = dist[r][c] + grid[nr][nc]
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return dist[m - 1][n - 1]
