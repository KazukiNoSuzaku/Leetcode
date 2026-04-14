# Author: Kaustav Ghosh
# 2312. Selling Pieces of Wood
# 2D DP: dp[h][w] = max profit from cutting an h x w board

class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        # dp[i][j] = max money from selling an i x j piece
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill in the direct sell prices
        for h, w, price in prices:
            dp[h][w] = price

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Try horizontal cuts
                for cut in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[cut][j] + dp[i - cut][j])
                # Try vertical cuts
                for cut in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][cut] + dp[i][j - cut])

        return dp[m][n]
