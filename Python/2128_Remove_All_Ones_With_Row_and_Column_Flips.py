# Author: Kaustav Ghosh
# Problem: Remove All Ones With Row and Column Flips
# Approach: Flipping columns to zero out the first row forces every other row to become all zeros only if it was identical to the first row or its exact complement. So the grid is clearable iff every row equals row 0 or its bitwise complement

class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        first = grid[0]
        complement = [1 - x for x in first]
        for row in grid:
            if row != first and row != complement:
                return False
        return True
