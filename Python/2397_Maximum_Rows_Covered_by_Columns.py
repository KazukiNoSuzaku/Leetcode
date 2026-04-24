from itertools import combinations

class Solution:
    def maximumRows(self, matrix: list[list[int]], numSelect: int) -> int:
        n = len(matrix[0])
        row_masks = [int(''.join(map(str, row)), 2) for row in matrix]
        best = 0
        for cols in combinations(range(n), numSelect):
            col_mask = sum(1 << (n - 1 - c) for c in cols)
            covered = sum(1 for rm in row_masks if rm & col_mask == rm)
            best = max(best, covered)
        return best
