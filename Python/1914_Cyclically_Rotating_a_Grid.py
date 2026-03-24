# Author: Kaustav Ghosh
# https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            # Extract the layer elements in order
            cells = []
            r1, c1 = layer, layer
            r2, c2 = m - 1 - layer, n - 1 - layer
            # Top row
            for c in range(c1, c2 + 1):
                cells.append(grid[r1][c])
            # Right column
            for r in range(r1 + 1, r2 + 1):
                cells.append(grid[r][c2])
            # Bottom row
            for c in range(c2 - 1, c1 - 1, -1):
                cells.append(grid[r2][c])
            # Left column
            for r in range(r2 - 1, r1, -1):
                cells.append(grid[r][c1])
            # Rotate
            length = len(cells)
            shift = k % length
            cells = cells[shift:] + cells[:shift]
            # Put back
            idx = 0
            for c in range(c1, c2 + 1):
                grid[r1][c] = cells[idx]
                idx += 1
            for r in range(r1 + 1, r2 + 1):
                grid[r][c2] = cells[idx]
                idx += 1
            for c in range(c2 - 1, c1 - 1, -1):
                grid[r2][c] = cells[idx]
                idx += 1
            for r in range(r2 - 1, r1, -1):
                grid[r][c1] = cells[idx]
                idx += 1
        return grid
