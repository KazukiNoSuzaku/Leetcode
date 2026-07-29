# Author: Kaustav Ghosh
# Problem: Get Biggest Three Rhombus Sums in a Grid
# Approach: For every center try each rhombus size that fits, summing the four diagonal edges (size 0 is the single cell). Collect distinct sums and return the three largest

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])  # size-0 rhombus (single cell)
                k = 1
                while r - k >= 0 and r + k < m and c - k >= 0 and c + k < n:
                    total = 0
                    for i in range(k):
                        total += grid[r - k + i][c + i]  # top -> right
                        total += grid[r + i][c + k - i]  # right -> bottom
                        total += grid[r + k - i][c - i]  # bottom -> left
                        total += grid[r - i][c - k + i]  # left -> top
                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]
