# Author: Kaustav Ghosh
# 1034. Coloring A Border
# https://leetcode.com/problems/coloring-a-border/

class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = set()
        border = set()

        def dfs(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))
            is_border = False
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == original:
                        dfs(nr, nc)
                    else:
                        is_border = True
                else:
                    is_border = True
            if is_border:
                border.add((r, c))

        dfs(row, col)
        for r, c in border:
            grid[r][c] = color
        return grid
