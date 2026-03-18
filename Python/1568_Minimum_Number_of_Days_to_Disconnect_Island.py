# Author: Kaustav Ghosh
# Problem: 1568 - Minimum Number of Days to Disconnect Island
# Approach: If disconnected return 0, check if removing 1 cell works, else 2

class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def count_islands():
            visited = [[False] * cols for _ in range(rows)]
            count = 0
            def dfs(r, c):
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    return
                if visited[r][c] or grid[r][c] == 0:
                    return
                visited[r][c] = True
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dfs(r + dr, c + dc)
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and not visited[r][c]:
                        count += 1
                        dfs(r, c)
            return count

        if count_islands() != 1:
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1

        return 2
