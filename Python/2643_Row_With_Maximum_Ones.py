class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        best_row, best_count = 0, 0
        for i, row in enumerate(mat):
            count = sum(row)
            if count > best_count:
                best_count = count
                best_row = i
        return [best_row, best_count]
