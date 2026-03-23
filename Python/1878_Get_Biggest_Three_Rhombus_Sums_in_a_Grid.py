# Author: Kaustav Ghosh
# Problem 1878: Get Biggest Three Rhombus Sums in a Grid

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])  # size 0 rhombus
                for size in range(1, m):
                    # Check bounds
                    if i - size < 0 or i + size >= m:
                        break
                    if j - size < 0 or j + size >= n:
                        break
                    total = 0
                    # Top to right
                    for k in range(size):
                        total += grid[i - size + k][j + k]
                    # Right to bottom
                    for k in range(size):
                        total += grid[i + k][j + size - k]
                    # Bottom to left
                    for k in range(size):
                        total += grid[i + size - k][j - k]
                    # Left to top
                    for k in range(size):
                        total += grid[i - k][j - size + k]
                    sums.add(total)
        result = sorted(sums, reverse=True)
        return result[:3]
