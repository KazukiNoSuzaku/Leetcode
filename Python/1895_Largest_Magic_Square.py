# Author: Kaustav Ghosh
# Problem: Largest Magic Square
# Approach: Row and column prefix sums make the sum of any horizontal or vertical run of a candidate square a single subtraction, so checking a square costs one pass along its side rather than a pass over its whole area. The two diagonals have no prefix structure worth building for a fifty by fifty grid, so they are added directly. Sizes are tried from the largest downwards and the first square that passes is returned, since a larger answer can never be found later, and a single cell is always magic so the search never comes up empty.

class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        across = [[0] * (cols + 1) for _ in range(rows)]
        down = [[0] * cols for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                across[r][c + 1] = across[r][c] + grid[r][c]
                down[r + 1][c] = down[r][c] + grid[r][c]

        def magic(top, left, size):
            target = across[top][left + size] - across[top][left]
            for r in range(top + 1, top + size):
                if across[r][left + size] - across[r][left] != target:
                    return False
            for c in range(left, left + size):
                if down[top + size][c] - down[top][c] != target:
                    return False
            if sum(grid[top + step][left + step] for step in range(size)) != target:
                return False
            if sum(grid[top + step][left + size - 1 - step] for step in range(size)) != target:
                return False
            return True

        for size in range(min(rows, cols), 1, -1):
            for top in range(rows - size + 1):
                for left in range(cols - size + 1):
                    if magic(top, left, size):
                        return size
        return 1
