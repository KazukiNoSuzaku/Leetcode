# Author: Kaustav Ghosh
# Problem: Shortest Path to Get Food
# Approach: Every step costs the same, so the fewest steps to any food cell is a breadth-first search from the starting cell, and because the search expands in order of distance the very first food cell it touches is the nearest one; there is no need to find all of them or to compare distances afterwards. Marking cells as visited the moment they are queued rather than when they are dequeued stops the same cell being enqueued twice. Exhausting the queue without meeting food means no food is reachable.

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

        seen = [[False] * cols for _ in range(rows)]
        seen[start[0]][start[1]] = True
        queue = deque([(start[0], start[1], 0)])
        while queue:
            r, c, steps = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < rows and 0 <= nc < cols) or seen[nr][nc]:
                    continue
                cell = grid[nr][nc]
                if cell == 'X':
                    continue
                if cell == '#':
                    return steps + 1
                seen[nr][nc] = True
                queue.append((nr, nc, steps + 1))
        return -1
