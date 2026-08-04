# Author: Kaustav Ghosh
# Problem: Nearest Exit from Entrance in Maze
# Approach: Breadth-first search from the entrance over empty cells. The first time we step onto a border cell that is not the entrance, that distance is the nearest exit. Mark cells visited by filling them

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        maze[sr][sc] = '+'
        q = deque([(sr, sc, 0)])
        while q:
            r, c, d = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return d + 1
                    maze[nr][nc] = '+'
                    q.append((nr, nc, d + 1))
        return -1
