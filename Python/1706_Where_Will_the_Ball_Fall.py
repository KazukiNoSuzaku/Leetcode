# Author: Kaustav Ghosh
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        result = []
        for col in range(n):
            c = col
            stuck = False
            for r in range(m):
                if grid[r][c] == 1:
                    if c + 1 >= n or grid[r][c + 1] == -1:
                        stuck = True
                        break
                    c += 1
                else:
                    if c - 1 < 0 or grid[r][c - 1] == 1:
                        stuck = True
                        break
                    c -= 1
            result.append(-1 if stuck else c)
        return result
