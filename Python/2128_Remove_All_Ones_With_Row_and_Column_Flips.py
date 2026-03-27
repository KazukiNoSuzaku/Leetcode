# Author: Kaustav Ghosh
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

# Premium Problem
# Check if all rows are either the same as the first row or the complement.
# If so, we can flip rows/columns to make all zeros.
#
# class Solution(object):
#     def removeOnes(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: bool
#         """
#         first = grid[0]
#         comp = [1 - x for x in first]
#         for row in grid:
#             if row != first and row != comp:
#                 return False
#         return True

class Solution(object):
    pass
