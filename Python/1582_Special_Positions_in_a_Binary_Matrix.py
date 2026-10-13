# Author: Kaustav Ghosh
# Problem: Special Positions in a Binary Matrix
# Approach: A position is special when it holds a one and is the only one in both its row and its column, so rather than rescanning a whole row and column for every candidate I total each row and each column once up front; then a cell qualifies precisely when its value is one and both of those totals are one. That turns a cubic check into two linear passes over the matrix.

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row_totals = [sum(row) for row in mat]
        col_totals = [sum(column) for column in zip(*mat)]
        special = 0
        for r, row in enumerate(mat):
            if row_totals[r] != 1:
                continue
            for c, value in enumerate(row):
                if value == 1 and col_totals[c] == 1:
                    special += 1
        return special
