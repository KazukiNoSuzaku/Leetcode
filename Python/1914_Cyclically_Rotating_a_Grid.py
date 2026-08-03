# Author: Kaustav Ghosh
# Problem: Cyclically Rotating a Grid
# Approach: Each concentric ring rotates independently. Collect a ring's cells in clockwise order, rotate the values left by k modulo the ring length (counter-clockwise shift), and write them back to the same cells

class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for l in range(layers):
            top, bottom, left, right = l, m - 1 - l, l, n - 1 - l
            cells = []
            for c in range(left, right + 1):
                cells.append((top, c))
            for r in range(top + 1, bottom + 1):
                cells.append((r, right))
            for c in range(right - 1, left - 1, -1):
                cells.append((bottom, c))
            for r in range(bottom - 1, top, -1):
                cells.append((r, left))

            vals = [grid[r][c] for r, c in cells]
            size = len(vals)
            shift = k % size
            rotated = vals[shift:] + vals[:shift]
            for (r, c), v in zip(cells, rotated):
                grid[r][c] = v
        return grid
