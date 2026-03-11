# Compute total surface area of 3D shape made from unit cubes in a grid.

# Author: Kaustav Ghosh

class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        res = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    res += 2 + 4 * grid[r][c]
                    if r > 0: res -= 2 * min(grid[r][c], grid[r-1][c])
                    if c > 0: res -= 2 * min(grid[r][c], grid[r][c-1])
        return res
