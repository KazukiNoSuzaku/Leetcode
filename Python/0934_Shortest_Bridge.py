# Find shortest bridge (flips) between two islands.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        island = []
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < n) or visited[r][c] or grid[r][c] == 0: return
            visited[r][c] = True
            island.append((r, c))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: dfs(r+dr, c+dc)
        found = False
        for r in range(n):
            if found: break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
        q = deque([(r, c, 0) for r, c in island])
        for r, c in island: visited[r][c] = True
        while q:
            r, c, dist = q.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] == 1: return dist
                    visited[nr][nc] = True
                    q.append((nr, nc, dist+1))
        return -1
