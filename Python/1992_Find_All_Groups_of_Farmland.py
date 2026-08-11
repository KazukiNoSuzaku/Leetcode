# Author: Kaustav Ghosh
# Problem: Find All Groups of Farmland
# Approach: A cell is a rectangle's top-left corner when it is land and the cells above and to its left are empty (or off-grid). From each corner, extend down and right along land to find the bottom-right corner

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        result = []
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1 and (r == 0 or land[r - 1][c] == 0) and (c == 0 or land[r][c - 1] == 0):
                    r2 = r
                    while r2 + 1 < m and land[r2 + 1][c] == 1:
                        r2 += 1
                    c2 = c
                    while c2 + 1 < n and land[r][c2 + 1] == 1:
                        c2 += 1
                    result.append([r, c, r2, c2])
        return result
