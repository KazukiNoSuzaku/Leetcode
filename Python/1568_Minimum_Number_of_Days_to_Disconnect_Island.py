# Author: Kaustav Ghosh
# Problem: Minimum Number of Days to Disconnect Island
# Approach: Answer is always 0, 1, or 2; check if already disconnected, else try removing each single land cell, otherwise 2 always suffices

class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def count_islands():
            seen = set()
            islands = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in seen:
                        islands += 1
                        stack = [(r, c)]
                        seen.add((r, c))
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in seen:
                                    seen.add((nx, ny))
                                    stack.append((nx, ny))
            return islands

        # already disconnected (0 islands or more than one)
        if count_islands() != 1:
            return 0

        # try removing a single cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        grid[r][c] = 1
                        return 1
                    grid[r][c] = 1

        return 2
