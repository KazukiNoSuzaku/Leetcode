# Author: Kaustav Ghosh
# https://leetcode.com/problems/shortest-path-to-get-food/
# Premium Problem
#
# Given a grid where '*' is your location, '#' is food, 'O' is free space,
# and 'X' is obstacle, find the shortest path length to any food cell.
# Return -1 if no food is reachable. Use BFS from start position.
#
# from collections import deque
#
# class Solution(object):
#     def getFood(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         rows, cols = len(grid), len(grid[0])
#         queue = deque()
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '*':
#                     queue.append((r, c, 0))
#                     grid[r][c] = 'X'
#                     break
#             if queue:
#                 break
#         while queue:
#             r, c, dist = queue.popleft()
#             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
#                     if grid[nr][nc] == '#':
#                         return dist + 1
#                     grid[nr][nc] = 'X'
#                     queue.append((nr, nc, dist + 1))
#         return -1

class Solution(object):
    pass
