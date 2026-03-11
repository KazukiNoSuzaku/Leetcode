# Find the maximum area of an island in a binary grid.

# Author: Kaustav Ghosh

class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        return max(dfs(r, c) for r in range(rows) for c in range(cols))
