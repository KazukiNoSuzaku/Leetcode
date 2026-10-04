# Author: Kaustav Ghosh
# Problem: Count Submatrices With All Ones
# Approach: For each cell record how many consecutive ones end there on its row. Fixing that cell as a submatrix's bottom-right corner and walking upwards, the widest allowed submatrix is the running minimum of those row lengths, and each height contributes exactly that many submatrices

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        run = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            length = 0
            for j in range(cols):
                length = length + 1 if mat[i][j] else 0
                run[i][j] = length
        total = 0
        for i in range(rows):
            for j in range(cols):
                width = run[i][j]
                for k in range(i, -1, -1):
                    width = min(width, run[k][j])
                    if width == 0:
                        break
                    total += width
        return total
