# Author: Kaustav Ghosh
# Problem: 2245. Maximum Trailing Zeros in a Cornered Path
# URL: https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
# Difficulty: Medium
#
# Approach:
# Precompute prefix sums of factors 2 and 5 along each row and column.
# At every cell, consider it as the corner of an L-shaped path going
# in four possible L-directions. Trailing zeros = min(total 2s, total 5s).

class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def count_factor(x, p):
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            return c

        # f2[i][j], f5[i][j] = factors of 2 and 5 in grid[i][j]
        f2 = [[0] * n for _ in range(m)]
        f5 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                f2[i][j] = count_factor(grid[i][j], 2)
                f5[i][j] = count_factor(grid[i][j], 5)

        # Row prefix sums (left to right)
        r2 = [[0] * (n + 1) for _ in range(m)]
        r5 = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r2[i][j + 1] = r2[i][j] + f2[i][j]
                r5[i][j + 1] = r5[i][j] + f5[i][j]

        # Column prefix sums (top to bottom)
        c2 = [[0] * n for _ in range(m + 1)]
        c5 = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                c2[i + 1][j] = c2[i][j] + f2[i][j]
                c5[i + 1][j] = c5[i][j] + f5[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                # left = row prefix up to and including (i,j)
                l2 = r2[i][j + 1]
                l5 = r5[i][j + 1]
                # right = row suffix from (i,j)
                ri2 = r2[i][n] - r2[i][j]
                ri5 = r5[i][n] - r5[i][j]
                # up = col prefix up to and including (i,j)
                u2 = c2[i + 1][j]
                u5 = c5[i + 1][j]
                # down = col suffix from (i,j)
                d2 = c2[m][j] - c2[i][j]
                d5 = c5[m][j] - c5[i][j]

                # 4 L-shapes: left+up, left+down, right+up, right+down
                # subtract (i,j) counted twice
                ans = max(ans, min(l2 + u2 - f2[i][j], l5 + u5 - f5[i][j]))
                ans = max(ans, min(l2 + d2 - f2[i][j], l5 + d5 - f5[i][j]))
                ans = max(ans, min(ri2 + u2 - f2[i][j], ri5 + u5 - f5[i][j]))
                ans = max(ans, min(ri2 + d2 - f2[i][j], ri5 + d5 - f5[i][j]))

        return ans
