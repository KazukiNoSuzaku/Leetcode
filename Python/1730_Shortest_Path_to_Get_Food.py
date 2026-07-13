# Author: Kaustav Ghosh
# Problem: Shortest Path to Get Food (Premium)
# Approach: Plain BFS from your position over free cells; the first food cell dequeued is at the minimum distance

from collections import deque

class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        start = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    start = (r, c)
                    break
            if start:
                break

        queue = deque([(start[0], start[1], 0)])
        seen = {start}
        while queue:
            r, c, dist = queue.popleft()
            if grid[r][c] == '#':
                return dist
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in seen and grid[nr][nc] != 'X'):
                    seen.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        return -1
