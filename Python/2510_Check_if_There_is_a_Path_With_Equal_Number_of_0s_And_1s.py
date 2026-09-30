# Author: Kaustav Ghosh
# Problem: Check if There is a Path With Equal Number of 0's And 1's
# Approach: Every path visits exactly m + n - 1 cells, so an even count is required before anything else. Track, for each cell, which totals of ones are reachable there, held as a bit set: a cell's reachable totals are those of the cells above and to the left, shifted up by its own value. The corner then only has to allow half the path length

class Solution(object):
    def isThereAPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        cells = rows + cols - 1
        if cells % 2:
            return False
        previous = [0] * cols
        for i in range(rows):
            current = [0] * cols
            for j in range(cols):
                value = grid[i][j]
                if i == 0 and j == 0:
                    current[0] = 1 << value
                    continue
                reachable = 0
                if i:
                    reachable |= previous[j]
                if j:
                    reachable |= current[j - 1]
                current[j] = reachable << value
            previous = current
        return bool(previous[cols - 1] >> (cells // 2) & 1)
