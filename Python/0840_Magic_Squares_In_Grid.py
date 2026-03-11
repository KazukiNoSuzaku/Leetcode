# Count 3x3 magic square subgrids (1-9 distinct, all sums equal 15).

# Author: Kaustav Ghosh

class Solution(object):
    def numMagicSquaresInside(self, grid):
        def is_magic(r, c):
            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in nums: return False
                    nums.add(grid[i][j])
            target = 15
            for i in range(r, r+3):
                if sum(grid[i][c+j] for j in range(3)) != target: return False
            for j in range(c, c+3):
                if sum(grid[r+i][j] for i in range(3)) != target: return False
            if grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2] != target: return False
            if grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c] != target: return False
            return True
        rows, cols = len(grid), len(grid[0])
        return sum(is_magic(r, c) for r in range(rows-2) for c in range(cols-2))
