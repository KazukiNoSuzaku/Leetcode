# You are given an m x n binary matrix image where 0 represents a white pixel and 1
# represents a black pixel. The black pixels are connected (i.e., there is only one black region).
# You are also given two integers x and y that represents the location of one of the black pixels.
# Return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# Example 1:
# Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
# Output: 6

# Example 2:
# Input: image = [["1"]], x = 0, y = 0
# Output: 1

# Constraints:
# m == image.length, n == image[i].length
# 1 <= m, n <= 100
# image[i][j] is either '0' or '1'.
# 1 <= x < m, 0 <= y < n
# image[x][y] == '1'

# Author: Kaustav Ghosh

class Solution(object):
    def minArea(self, image, x, y):
        m, n = len(image), len(image[0])

        def col_has_black(col):
            return any(image[r][col] == '1' for r in range(m))

        def row_has_black(row):
            return any(image[row][c] == '1' for c in range(n))

        def bin_search(lo, hi, check, want_first):
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid) == want_first:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        top    = bin_search(0, x, row_has_black, True)
        bottom = bin_search(x, m - 1, row_has_black, False)
        left   = bin_search(0, y, col_has_black, True)
        right  = bin_search(y, n - 1, col_has_black, False)

        return (bottom - top + 1) * (right - left + 1)
