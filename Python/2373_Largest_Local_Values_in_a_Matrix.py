# Author: Kaustav Ghosh
# Problem: Largest Local Values in a Matrix
# Approach: Every 3x3 block of the n x n grid produces one cell of the (n - 2) x (n - 2) answer, so take the maximum over each block directly

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        return [[max(grid[r + dr][c + dc] for dr in range(3) for dc in range(3))
                 for c in range(n - 2)] for r in range(n - 2)]
