# Author: Kaustav Ghosh
# Flatten grid, shift by k, reshape back to 2D

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % len(flat)
        flat = flat[-k:] + flat[:-k] if k else flat
        return [flat[i * n:(i + 1) * n] for i in range(m)]
