# Author: Kaustav Ghosh
# Problem: Cyclically Rotating a Grid
# Approach: The rings rotate independently, so each is lifted out into a flat list by walking it once in order, rotated by k reduced modulo its own length, and written back along the same path. Reducing k is what keeps a billion rotations cheap, and because the ring is read and written through the same list of coordinates the rotation direction cannot drift between the two halves of the operation.

class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        result = [list(row) for row in grid]

        for layer in range(min(rows, cols) // 2):
            top, bottom = layer, rows - 1 - layer
            left, right = layer, cols - 1 - layer

            path = []
            for c in range(left, right):
                path.append((top, c))
            for r in range(top, bottom):
                path.append((r, right))
            for c in range(right, left, -1):
                path.append((bottom, c))
            for r in range(bottom, top, -1):
                path.append((r, left))

            values = [result[r][c] for r, c in path]
            shift = k % len(values)
            values = values[shift:] + values[:shift]
            for (r, c), value in zip(path, values):
                result[r][c] = value
        return result
