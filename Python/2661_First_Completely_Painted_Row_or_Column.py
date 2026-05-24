class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        row_count = [0] * m
        col_count = [0] * n

        for idx, val in enumerate(arr):
            r, c = pos[val]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] == m:
                return idx

        return -1
