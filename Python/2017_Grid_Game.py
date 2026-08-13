# Author: Kaustav Ghosh
# Problem: Grid Game
# Approach: The first robot drops to the bottom row at some column c, zeroing that path. The second robot's best remaining is either the top row right of c or the bottom row left of c. The first robot picks c to minimize that maximum

class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_right = sum(grid[0]) - grid[0][0]
        bottom_left = 0
        best = float('inf')
        for c in range(n):
            best = min(best, max(top_right, bottom_left))
            if c + 1 < n:
                top_right -= grid[0][c + 1]
            bottom_left += grid[1][c]
        return best
