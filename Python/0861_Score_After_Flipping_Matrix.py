# Maximize score (binary number rows) by toggling rows then columns.

# Author: Kaustav Ghosh

class Solution(object):
    def matrixScore(self, grid):
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols): grid[r][c] ^= 1
        res = 0
        for c in range(cols):
            ones = sum(grid[r][c] for r in range(rows))
            res += max(ones, rows - ones) * (1 << (cols - c - 1))
        return res
