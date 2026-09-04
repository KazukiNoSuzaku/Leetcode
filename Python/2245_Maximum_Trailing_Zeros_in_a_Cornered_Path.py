# Author: Kaustav Ghosh
# Problem: Maximum Trailing Zeros in a Cornered Path
# Approach: Trailing zeros of a product equal min(#factor-2, #factor-5). Precompute per-cell counts of 2s and 5s, plus row and column prefix sums of each. For every cell taken as the single turning corner, combine a horizontal arm (left or right, including the corner) with a vertical arm (up or down, excluding the corner); the best of the four combinations over all corners is the answer

class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        H, W = len(grid), len(grid[0])

        def count(x, p):
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            return c

        two = [[count(grid[r][c], 2) for c in range(W)] for r in range(H)]
        five = [[count(grid[r][c], 5) for c in range(W)] for r in range(H)]

        # row prefix sums (inclusive), col prefix sums (inclusive)
        row2 = [[0] * W for _ in range(H)]
        row5 = [[0] * W for _ in range(H)]
        col2 = [[0] * W for _ in range(H)]
        col5 = [[0] * W for _ in range(H)]
        for r in range(H):
            for c in range(W):
                row2[r][c] = two[r][c] + (row2[r][c - 1] if c > 0 else 0)
                row5[r][c] = five[r][c] + (row5[r][c - 1] if c > 0 else 0)
        for c in range(W):
            for r in range(H):
                col2[r][c] = two[r][c] + (col2[r - 1][c] if r > 0 else 0)
                col5[r][c] = five[r][c] + (col5[r - 1][c] if r > 0 else 0)

        ans = 0
        for r in range(H):
            for c in range(W):
                t2, t5 = two[r][c], five[r][c]
                left2 = row2[r][c]
                left5 = row5[r][c]
                right2 = row2[r][W - 1] - row2[r][c] + t2
                right5 = row5[r][W - 1] - row5[r][c] + t5
                up2 = col2[r][c] - t2
                up5 = col5[r][c] - t5
                down2 = col2[H - 1][c] - col2[r][c]
                down5 = col5[H - 1][c] - col5[r][c]
                for h2, h5 in ((left2, left5), (right2, right5)):
                    for v2, v5 in ((up2, up5), (down2, down5)):
                        ans = max(ans, min(h2 + v2, h5 + v5))
        return ans
