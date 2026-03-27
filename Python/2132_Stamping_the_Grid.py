# Author: Kaustav Ghosh
# https://leetcode.com/problems/stamping-the-grid/

# Premium Problem
# Use 2D prefix sums to check if a stamp-sized rectangle is all zeros,
# then use a 2D difference array to mark stamped cells.
# Finally verify all zero cells are covered by at least one stamp.
#
# class Solution(object):
#     def possibleToStamp(self, grid, stampHeight, stampWidth):
#         """
#         :type grid: List[List[int]]
#         :type stampHeight: int
#         :type stampWidth: int
#         :rtype: bool
#         """
#         m, n = len(grid), len(grid[0])
#         # Build prefix sum of grid
#         pre = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(m):
#             for j in range(n):
#                 pre[i+1][j+1] = grid[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
#         # Difference array for stamps placed
#         diff = [[0] * (n + 2) for _ in range(m + 2)]
#         for i in range(stampHeight, m + 1):
#             for j in range(stampWidth, n + 1):
#                 # check rectangle [i-stampHeight..i-1][j-stampWidth..j-1]
#                 total = pre[i][j] - pre[i-stampHeight][j] - pre[i][j-stampWidth] + pre[i-stampHeight][j-stampWidth]
#                 if total == 0:
#                     r, c = i - stampHeight, j - stampWidth
#                     diff[r][c] += 1
#                     diff[r][j] -= 1
#                     diff[i][c] -= 1
#                     diff[i][j] += 1
#         # Compute prefix sum of diff and verify
#         for i in range(m):
#             for j in range(n):
#                 if i > 0: diff[i][j] += diff[i-1][j]
#                 if j > 0: diff[i][j] += diff[i][j-1]
#                 if i > 0 and j > 0: diff[i][j] -= diff[i-1][j-1]
#                 if grid[i][j] == 0 and diff[i][j] == 0:
#                     return False
#         return True

class Solution(object):
    pass
