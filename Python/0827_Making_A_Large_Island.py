# Flip at most one 0 to 1 and find the largest island size.

# Author: Kaustav Ghosh

class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        def dfs(r, c, idx):
            grid[r][c] = idx
            size = 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    size += dfs(nr, nc, idx)
            return size
        island_size = {}
        idx = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_size[idx] = dfs(r, c, idx)
                    idx += 1
        res = max(island_size.values()) if island_size else 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    total = 1
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1 and grid[nr][nc] not in seen:
                            seen.add(grid[nr][nc])
                            total += island_size[grid[nr][nc]]
                    res = max(res, total)
        return res
