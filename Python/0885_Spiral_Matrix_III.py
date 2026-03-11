# Return grid positions in spiral order starting from (rStart, cStart).

# Author: Kaustav Ghosh

class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        r, c = rStart, cStart
        res = []
        step = 1
        d = 0
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r += dirs[d][0]; c += dirs[d][1]
                d = (d + 1) % 4
            step += 1
        return res
