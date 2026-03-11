# Find total sum of heights that can be increased without changing skyline from any direction.

# Author: Kaustav Ghosh

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
        return sum(min(row_max[r], col_max[c]) - grid[r][c]
                   for r in range(len(grid)) for c in range(len(grid[0])))
