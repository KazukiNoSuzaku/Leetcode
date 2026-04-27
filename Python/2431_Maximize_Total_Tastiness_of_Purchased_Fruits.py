# Premium problem
# 2D knapsack: dp[money_left][coupons_left] = max tastiness
# Each fruit: buy at full price, buy with coupon (half price, rounded down), or skip.

class Solution:
    def maxTastiness(self, price: list[int], tastiness: list[int],
                     maxAmount: int, maxCoupons: int) -> int:
        dp = [[0] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        for p, t in zip(price, tastiness):
            half = p // 2
            for m in range(maxAmount, -1, -1):
                for c in range(maxCoupons, -1, -1):
                    if m >= p:
                        dp[m][c] = max(dp[m][c], dp[m - p][c] + t)
                    if c > 0 and m >= half:
                        dp[m][c] = max(dp[m][c], dp[m - half][c - 1] + t)
        return dp[maxAmount][maxCoupons]
