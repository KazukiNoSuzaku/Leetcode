# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Author: Kaustav Ghosh

class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        diagonals = {}
        for i in range(m):
            for j in range(n):
                d = i + j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(mat[i][j])
        res = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                res.extend(reversed(diagonals[d]))
            else:
                res.extend(diagonals[d])
        return res
