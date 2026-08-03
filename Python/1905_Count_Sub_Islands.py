# Author: Kaustav Ghosh
# Problem: Count Sub Islands
# Approach: Flood fill each island of grid2. While visiting, note whether any cell of it is water in grid1; an island counts only if every one of its cells is land in grid1

class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid2), len(grid2[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] != 1:
                    continue
                stack = [(i, j)]
                grid2[i][j] = 0
                is_sub = True
                while stack:
                    r, c = stack.pop()
                    if grid1[r][c] == 0:
                        is_sub = False
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                            grid2[nr][nc] = 0
                            stack.append((nr, nc))
                if is_sub:
                    count += 1
        return count
