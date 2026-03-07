# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result
# of mat1 x mat2. You may assume that multiplication is always possible.

# Example 1:
# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]

# Constraints:
# m == mat1.length, k == mat1[i].length == mat2.length, n == mat2[i].length
# 1 <= m, n, k <= 100
# -100 <= mat1[i][j], mat2[i][j] <= 100

# Author: Kaustav Ghosh

class Solution(object):
    def multiply(self, mat1, mat2):
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for p in range(k):
                if mat1[i][p] == 0:
                    continue
                for j in range(n):
                    res[i][j] += mat1[i][p] * mat2[p][j]
        return res
