# Author: Kaustav Ghosh
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            r, c, dist = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return dist + 1
                    maze[nr][nc] = '+'
                    q.append((nr, nc, dist + 1))
        return -1
