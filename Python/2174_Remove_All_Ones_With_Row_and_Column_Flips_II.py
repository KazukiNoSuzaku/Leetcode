# Author: Kaustav Ghosh
# Problem: 2174. Remove All Ones With Row and Column Flips II
# URL: https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/
# Premium Problem
# Approach: BFS/BitmaskDP on the grid state encoded as a bitmask.
#           Each operation selects a cell (r,c) where grid[r][c]==1 and flips
#           all cells in row r and column c. BFS minimizes operations to reach 0.
#
# class Solution(object):
#     def removeOnes(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         from collections import deque
#         m, n = len(grid), len(grid[0])
#         start = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     start |= (1 << (i * n + j))
#         if start == 0:
#             return 0
#         visited = {start}
#         queue = deque([(start, 0)])
#         while queue:
#             state, ops = queue.popleft()
#             for r in range(m):
#                 for c in range(n):
#                     if state & (1 << (r * n + c)):
#                         new_state = state
#                         # flip entire row r
#                         for j in range(n):
#                             new_state ^= (1 << (r * n + j))
#                         # flip entire col c
#                         for i in range(m):
#                             new_state ^= (1 << (i * n + c))
#                         if new_state == 0:
#                             return ops + 1
#                         if new_state not in visited:
#                             visited.add(new_state)
#                             queue.append((new_state, ops + 1))
#         return -1

class Solution(object):
    pass
