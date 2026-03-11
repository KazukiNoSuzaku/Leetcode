# Calculate total projection areas on three planes of a 3D shape.

# Author: Kaustav Ghosh

class Solution(object):
    def projectionArea(self, grid):
        n = len(grid)
        top = sum(1 for r in range(n) for c in range(n) if grid[r][c])
        front = sum(max(grid[r][c] for r in range(n)) for c in range(n))
        side = sum(max(grid[r][c] for c in range(n)) for r in range(n))
        return top + front + side
