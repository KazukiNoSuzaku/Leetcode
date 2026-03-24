# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-sub-islands/

class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid2), len(grid2[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            is_sub = grid1[i][j] == 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not dfs(i + di, j + dj):
                    is_sub = False
            return is_sub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count
