# An n x n grid has '/', '\', or ' ' in each cell. Count the regions formed.

# Author: Kaustav Ghosh

class Solution(object):
    def regionsBySlashes(self, grid):
        n = len(grid)
        size = 4 * n * n
        parent = list(range(size))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                c = grid[i][j]
                if c == '/':
                    union(base+0, base+3)
                    union(base+1, base+2)
                elif c == chr(92):
                    union(base+0, base+1)
                    union(base+2, base+3)
                else:
                    union(base+0, base+1)
                    union(base+1, base+2)
                    union(base+2, base+3)
                if j + 1 < n:
                    union(base+1, 4*(i*n+j+1)+3)
                if i + 1 < n:
                    union(base+2, 4*((i+1)*n+j)+0)
        return sum(find(i) == i for i in range(size))
