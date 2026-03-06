# You are given an m x n grid rooms initialized with these three possible values:
# -1 A wall or an obstacle.
# 0 A gate.
# INF (2^31 - 1) Infinity means an empty room.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
#                 [2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Constraints:
# m == rooms.length, n == rooms[i].length
# 1 <= m, n <= 250

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
