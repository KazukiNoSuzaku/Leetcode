# Find amount of champagne in row r, glass c after pouring poured cups.

# Author: Kaustav Ghosh

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        tower = [[0.0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured
        for r in range(query_row):
            for c in range(r + 1):
                overflow = max(0, tower[r][c] - 1)
                tower[r+1][c] += overflow / 2.0
                tower[r+1][c+1] += overflow / 2.0
        return min(1.0, tower[query_row][query_glass])
