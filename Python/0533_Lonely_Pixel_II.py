# Given an m x n picture and integer N, return the number of black lonely pixels.
# A black lonely pixel is a 'B' at (r,c) such that row r has exactly N 'B's and
# for every 'B' in row r, the column containing it has exactly N 'B's all in the same rows.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findLonelyPixel(self, picture, N):
        m, n = len(picture), len(picture[0])
        col_rows = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    col_rows[j].append(i)
        res = 0
        for i in range(m):
            row_b = [j for j in range(n) if picture[i][j] == 'B']
            if len(row_b) != N:
                continue
            for j in row_b:
                if len(col_rows[j]) == N and all(col_rows[j] == col_rows[row_b[0]] for _ in [1]):
                    pass
                if len(col_rows[j]) == N and col_rows[j] == sorted(col_rows[row_b[0]]):
                    res += 1
        return res
