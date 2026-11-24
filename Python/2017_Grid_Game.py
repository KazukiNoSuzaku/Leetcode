# Author: Kaustav Ghosh
# Problem: Grid Game
# Approach: With only two rows, a path from the top-left to the bottom-right is determined entirely by the column where it drops from the top row to the bottom row, so the first robot's whole strategy is that single choice. Once it has emptied its path, the second robot can only collect either the top-row cells strictly to the right of the drop column or the bottom-row cells strictly to its left, and it will take the larger of the two. So the first robot picks the drop column minimising that larger amount, which one sweep finds while maintaining the shrinking suffix of the top row and the growing prefix of the bottom row.

class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_remaining = sum(grid[0]) - grid[0][0]
        bottom_collected = 0
        best = None
        for column in range(len(grid[0])):
            if column > 0:
                top_remaining -= grid[0][column]
                bottom_collected += grid[1][column - 1]
            second = top_remaining if top_remaining > bottom_collected else bottom_collected
            if best is None or second < best:
                best = second
        return best
