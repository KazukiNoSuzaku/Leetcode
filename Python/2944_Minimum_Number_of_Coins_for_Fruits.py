from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i] = min coins to acquire fruits i..n (1-indexed), given fruit i must be bought
        dp = [0] * (n + 1)
        for i in range(n, 0, -1):
            if 2 * i >= n:
                dp[i] = prices[i - 1]
            else:
                dp[i] = prices[i - 1] + min(dp[j] for j in range(i + 1, 2 * i + 2))
        return dp[1]
