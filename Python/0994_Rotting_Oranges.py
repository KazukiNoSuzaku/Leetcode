# In a grid, 0=empty, 1=fresh, 2=rotten. Each minute, rotten oranges spread.
# Return minimum minutes until no fresh orange remains, or -1 if impossible.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: fresh += 1
        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        return minutes if fresh == 0 else -1
