# Author: Kaustav Ghosh
# https://leetcode.com/problems/largest-magic-square/

class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # Prefix sums for rows and columns
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]

        def check(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_sum[i][j + k] - row_sum[i][j]
                    valid = True
                    # Check all rows
                    for r in range(i, i + k):
                        if row_sum[r][j + k] - row_sum[r][j] != target:
                            valid = False
                            break
                    if not valid:
                        continue
                    # Check all columns
                    for c in range(j, j + k):
                        if col_sum[i + k][c] - col_sum[i][c] != target:
                            valid = False
                            break
                    if not valid:
                        continue
                    # Check main diagonal
                    d1 = sum(grid[i + x][j + x] for x in range(k))
                    if d1 != target:
                        continue
                    # Check anti-diagonal
                    d2 = sum(grid[i + x][j + k - 1 - x] for x in range(k))
                    if d2 != target:
                        continue
                    return True
            return False

        for k in range(min(m, n), 0, -1):
            if check(k):
                return k
        return 1
