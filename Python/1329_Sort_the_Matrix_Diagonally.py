# Sort each diagonal of a matrix in ascending order from top-left to bottom-right.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        diags = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diags[i - j].append(mat[i][j])
        for key in diags:
            diags[key].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i - j].pop()
        return mat
