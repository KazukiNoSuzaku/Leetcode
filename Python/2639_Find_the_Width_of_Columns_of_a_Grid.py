class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        n = len(grid[0])
        return [max(len(str(grid[i][j])) for i in range(len(grid))) for j in range(n)]
