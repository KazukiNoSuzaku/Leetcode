# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/
# Premium - Bipartite matching (maximum independent set)
#
# class Solution(object):
#     def minimumOperations(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m, n = len(grid), len(grid[0])
#         match = {}
#
#         def dfs(u, visited):
#             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nr, nc = u[0] + dr, u[1] + dc
#                 if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in visited:
#                     visited.add((nr, nc))
#                     if (nr, nc) not in match or dfs(match[(nr, nc)], visited):
#                         match[(nr, nc)] = u
#                         match[u] = (nr, nc)
#                         return True
#             return False
#
#         result = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1 and (r + c) % 2 == 0:
#                     visited = set()
#                     if dfs((r, c), visited):
#                         result += 1
#         return result

class Solution(object):
    pass
