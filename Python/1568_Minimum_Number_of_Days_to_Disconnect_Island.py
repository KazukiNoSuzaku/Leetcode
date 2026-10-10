# Author: Kaustav Ghosh
# Problem: Minimum Number of Days to Disconnect Island
# Approach: The answer is never more than two, because flooding the two neighbours of any corner-most land cell always cuts it loose, so I only have to distinguish zero, one and two: zero when the grid is already not a single island, one when flooding some single land cell leaves it not a single island, and two otherwise. Counting islands is a plain flood fill, and "disconnected" covers both zero islands and two or more.

class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def islands():
            seen = [[False] * cols for _ in range(rows)]
            found = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and not seen[r][c]:
                        found += 1
                        if found > 1:
                            return found
                        stack = [(r, c)]
                        seen[r][c] = True
                        while stack:
                            x, y = stack.pop()
                            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not seen[nx][ny]:
                                    seen[nx][ny] = True
                                    stack.append((nx, ny))
            return found

        if islands() != 1:
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if islands() != 1:
                        grid[r][c] = 1
                        return 1
                    grid[r][c] = 1
        return 2
