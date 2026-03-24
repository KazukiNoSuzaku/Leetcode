# Author: Kaustav Ghosh
# Problem 1992: Find All Groups of Farmland

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # Find bottom-right corner
                    r, c = i, j
                    while r + 1 < m and land[r + 1][j] == 1:
                        r += 1
                    while c + 1 < n and land[i][c + 1] == 1:
                        c += 1
                    result.append([i, j, r, c])
                    # Mark as visited
                    for x in range(i, r + 1):
                        for y in range(j, c + 1):
                            land[x][y] = 0
        return result
