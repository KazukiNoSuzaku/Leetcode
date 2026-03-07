# Given a 2D matrix matrix, handle multiple queries of the following types:
# 1. Update the value of a cell in matrix.
# 2. Calculate the sum of the elements of matrix inside the rectangle defined by
#    its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class with update and sumRegion.

# Example 1:
# Input: ["NumMatrix","sumRegion","update","sumRegion"]
#        [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]
# Output: [null,8,null,10]

# Constraints:
# m == matrix.length, n == matrix[i].length
# 1 <= m, n <= 200
# At most 10^4 calls will be made to update and sumRegion.

# Author: Kaustav Ghosh

class NumMatrix(object):
    def __init__(self, matrix):
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def _query(self, row, col):
        s = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s

    def sumRegion(self, row1, col1, row2, col2):
        return (self._query(row2 + 1, col2 + 1) - self._query(row1, col2 + 1)
                - self._query(row2 + 1, col1) + self._query(row1, col1))
