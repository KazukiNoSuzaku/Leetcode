# Author: Kaustav Ghosh
# Problem: Maximum Rows Covered by Columns
# Approach: There are at most 12 columns, so try every choice of numSelect columns. Store each row's ones as a bitmask; a row is covered when none of its bits fall outside the chosen mask, and the best count over all choices is the answer

from itertools import combinations


class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        rows = [sum(bit << j for j, bit in enumerate(row)) for row in matrix]
        best = 0
        for cols in combinations(range(len(matrix[0])), numSelect):
            chosen = sum(1 << j for j in cols)
            best = max(best, sum(1 for mask in rows if mask & ~chosen == 0))
        return best
