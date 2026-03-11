# Find shortest path to collect all keys in a grid; doors require matching keys.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        rows, cols = len(grid), len(grid[0])
        keys = sum(1 for row in grid for c in row if c.islower())
        full = (1 << keys) - 1
        start = next((r, c, 0) for r in range(rows) for c in range(cols) if grid[r][c] == '@')
        q = deque([(start[0], start[1], 0, 0)])
        visited = {(start[0], start[1], 0)}
        while q:
            r, c, ks, steps = q.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cell = grid[nr][nc]
                    if cell == '#': continue
                    if cell.isupper() and not (ks >> (ord(cell.lower())-ord('a')) & 1): continue
                    nks = ks | (1 << (ord(cell)-ord('a'))) if cell.islower() else ks
                    if nks == full: return steps + 1
                    if (nr, nc, nks) not in visited:
                        visited.add((nr, nc, nks))
                        q.append((nr, nc, nks, steps + 1))
        return -1
