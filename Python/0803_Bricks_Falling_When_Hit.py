# After each hit, count bricks that fall (not connected to top).

# Author: Kaustav Ghosh

class Solution(object):
    def hitBricks(self, grid, hits):
        rows, cols = len(grid), len(grid[0])
        g = [row[:] for row in grid]
        for r, c in hits: g[r][c] = 0
        parent = list(range(rows * cols + 1))
        size = [1] * (rows * cols + 1)
        roof = rows * cols
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if size[px] < size[py]: px, py = py, px
            parent[py] = px; size[px] += size[py]
        def idx(r, c): return r * cols + c
        for c in range(cols):
            if g[0][c]: union(idx(0, c), roof)
        for r in range(rows):
            for c in range(cols):
                if g[r][c]:
                    if r > 0 and g[r-1][c]: union(idx(r,c), idx(r-1,c))
                    if c > 0 and g[r][c-1]: union(idx(r,c), idx(r,c-1))
        res = []
        for r, c in reversed(hits):
            if grid[r][c] == 0: res.append(0); continue
            before = size[find(roof)]
            g[r][c] = 1
            if r == 0: union(idx(r,c), roof)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and g[nr][nc]:
                    union(idx(r,c), idx(nr,nc))
            after = size[find(roof)]
            res.append(max(0, after - before - 1))
        return res[::-1]
