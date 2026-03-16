# Author: Kaustav Ghosh
# Problem: Count Negative Numbers in a Sorted Matrix
# Approach: Staircase from top-right corner, count negatives per row

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        col = n - 1
        for row in range(m):
            while col >= 0 and grid[row][col] < 0:
                col -= 1
            count += n - col - 1
        return count
