# Author: Kaustav Ghosh
# 2319. Check if Matrix Is X-Matrix
# Diagonals must be nonzero, all off-diagonal elements must be zero

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)

        for i in range(n):
            for j in range(n):
                on_diagonal = (i == j) or (i + j == n - 1)
                if on_diagonal:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True
