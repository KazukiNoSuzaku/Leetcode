# Author: Kaustav Ghosh
# Problem 2017: Grid Game

class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        # Robot 1 goes down at some column i
        # Robot 2 gets max of: top row suffix after i, or bottom row prefix before i
        top_sum = sum(grid[0])
        bottom_sum = 0
        result = float('inf')
        for i in range(n):
            top_sum -= grid[0][i]
            result = min(result, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]
        return result
