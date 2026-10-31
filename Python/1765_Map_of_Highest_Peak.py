# Author: Kaustav Ghosh
# Problem: Map of Highest Peak
# Approach: Heights may differ by at most one between neighbours and every water cell is fixed at zero, so a cell can never be higher than its distance to the nearest water cell, and setting every cell to exactly that distance satisfies the constraint while maximising the peak. That distance field is what a breadth-first search started from all water cells at once produces, each layer being one taller than the last, so a single sweep of the queue fills the grid.

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        frontier = []
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    height[r][c] = 0
                    frontier.append((r, c))

        level = 0
        while frontier:
            level += 1
            nxt = []
            for r, c in frontier:
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] < 0:
                        height[nr][nc] = level
                        nxt.append((nr, nc))
            frontier = nxt
        return height
