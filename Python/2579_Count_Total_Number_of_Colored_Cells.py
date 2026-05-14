class Solution:
    def coloredCells(self, n: int) -> int:
        # Diamond expands by 4k cells at minute k; total = 1 + 4*(1+2+...+(n-1)) = 2n²-2n+1.
        return 2 * n * n - 2 * n + 1
