# Author: Kaustav Ghosh
# Precompute horizontal and vertical consecutive 1s, check all possible square borders

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # hor[i][j] = consecutive 1s ending at (i,j) going left
        # ver[i][j] = consecutive 1s ending at (i,j) going up
        hor = [[0] * n for _ in range(m)]
        ver = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = (hor[i][j - 1] if j > 0 else 0) + 1
                    ver[i][j] = (ver[i - 1][j] if i > 0 else 0) + 1

        result = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                side = min(hor[i][j], ver[i][j])
                while side > result:
                    if ver[i][j - side + 1] >= side and hor[i - side + 1][j] >= side:
                        result = side
                        break
                    side -= 1
        return result * result
