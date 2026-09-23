# Author: Kaustav Ghosh
# Problem: Maximum Sum of an Hourglass
# Approach: An hourglass is fixed by its top-left corner, covering the full top and bottom rows of a 3x3 block plus only the centre of the middle row, so score every valid corner and keep the largest

class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return max(sum(grid[r][c:c + 3]) + grid[r + 1][c + 1] + sum(grid[r + 2][c:c + 3])
                   for r in range(len(grid) - 2) for c in range(len(grid[0]) - 2))
