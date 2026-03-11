# On a grid with obstacles, walk from start (1) to end (2) visiting every empty cell.
# Return the number of such 4-directional paths.

# Author: Kaustav Ghosh

class Solution(object):
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        empty = sum(grid[i][j] != -1 for i in range(m) for j in range(n))
        start = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == 1)
        self.res = 0
        def dfs(x, y, count):
            if grid[x][y] == 2:
                if count == empty: self.res += 1
                return
            tmp = grid[x][y]
            grid[x][y] = -1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    dfs(nx, ny, count + 1)
            grid[x][y] = tmp
        dfs(start[0], start[1], 1)
        return self.res
