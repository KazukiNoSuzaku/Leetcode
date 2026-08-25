# Author: Kaustav Ghosh
# Problem: Stamping the Grid
# Approach: A stamp can be placed with top-left (i,j) only if that h*w region is entirely empty (checked via a 2D prefix sum of occupied cells). Mark every cell covered by some valid placement using a 2D difference array, then verify every empty cell is covered

class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        h, w = stampHeight, stampWidth

        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = grid[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        def region_sum(r1, c1, r2, c2):  # inclusive rectangle
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - h + 1):
            for j in range(n - w + 1):
                if region_sum(i, j, i + h - 1, j + w - 1) == 0:
                    diff[i][j] += 1
                    diff[i + h][j] -= 1
                    diff[i][j + w] -= 1
                    diff[i + h][j + w] += 1

        cover = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cover[i + 1][j + 1] = diff[i][j] + cover[i][j + 1] + cover[i + 1][j] - cover[i][j]
                if grid[i][j] == 0 and cover[i + 1][j + 1] == 0:
                    return False
        return True
