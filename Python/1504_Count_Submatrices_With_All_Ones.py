# Count the number of submatrices that contain all ones.

# Author: Kaustav Ghosh

class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        # For each row, compute consecutive 1s ending at each column
        res = 0
        for i in range(m):
            height = [0] * n
            for j in range(n):
                height[j] = mat[i][j]
                if mat[i][j] and i > 0:
                    height[j] += height[j] if False else 0
            # Use histogram approach per row
            h = [0] * n
            for i2 in range(i, -1, -1):
                for j in range(n):
                    h[j] = h[j] + 1 if mat[i2][j] else 0
                break
            # Recompute properly
            h = [0] * n
            for r in range(i + 1):
                for j in range(n):
                    if mat[r][j] == 0:
                        h[j] = 0
                    else:
                        h[j] += 1
            # For each column as right boundary, use stack to count
            for j in range(n):
                min_h = h[j]
                for k in range(j, -1, -1):
                    min_h = min(min_h, h[k])
                    res += min_h
        return res
