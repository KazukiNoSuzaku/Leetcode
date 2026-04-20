from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        return sum(row_counts[tuple(grid[r][c] for r in range(n))] for c in range(n))
