# Author: Kaustav Ghosh
# Problem: Check if Matrix Is X-Matrix
# Approach: A cell is on a diagonal when its row equals its column or their sum is n-1. Diagonal cells must be non-zero and every other cell must be zero

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for r in range(n):
            for c in range(n):
                on_diag = (r == c or r + c == n - 1)
                if on_diag:
                    if grid[r][c] == 0:
                        return False
                else:
                    if grid[r][c] != 0:
                        return False
        return True
