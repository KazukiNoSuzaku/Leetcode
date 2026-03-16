# Author: Kaustav Ghosh
# Problem: Minimum Cost to Make at Least One Valid Path in a Grid
# Approach: 0-1 BFS using deque

from collections import deque

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # direction: 1=right, 2=left, 3=down, 4=up
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0, 0)])
        while dq:
            cost, r, c = dq.popleft()
            if cost > dist[r][c]:
                continue
            for d, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    w = 0 if grid[r][c] == d else 1
                    if cost + w < dist[nr][nc]:
                        dist[nr][nc] = cost + w
                        if w == 0:
                            dq.appendleft((cost, nr, nc))
                        else:
                            dq.append((cost + 1, nr, nc))
        return dist[m - 1][n - 1]
