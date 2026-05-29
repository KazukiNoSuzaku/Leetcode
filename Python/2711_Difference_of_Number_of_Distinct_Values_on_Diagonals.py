class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for diff in range(-(n - 1), m):
            cells = [(i, i - diff) for i in range(max(0, diff), min(m, n + diff))]
            seen = set()
            prefix = []
            for i, j in cells:
                prefix.append(len(seen))
                seen.add(grid[i][j])
            seen = set()
            suffix = [0] * len(cells)
            for k in range(len(cells) - 1, -1, -1):
                suffix[k] = len(seen)
                seen.add(grid[cells[k][0]][cells[k][1]])
            for k, (i, j) in enumerate(cells):
                ans[i][j] = abs(prefix[k] - suffix[k])
        return ans
