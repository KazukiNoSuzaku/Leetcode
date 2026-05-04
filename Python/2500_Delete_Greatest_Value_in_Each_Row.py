class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for row in grid:
            row.sort()
        # At each step we remove the column maximum; sorted rows make this column-wise max
        return sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0])))
