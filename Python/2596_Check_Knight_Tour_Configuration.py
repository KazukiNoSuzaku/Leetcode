class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        n = len(grid)
        pos = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)
        for step in range(1, n * n):
            r1, c1 = pos[step - 1]
            r2, c2 = pos[step]
            dr, dc = abs(r2 - r1), abs(c2 - c1)
            if sorted([dr, dc]) != [1, 2]:
                return False
        return True
