# Author: Kaustav Ghosh
# Problem: Maximize Total Tastiness of Purchased Fruits
# Approach: A knapsack over two budgets at once, money and coupons. dp[amount][coupons] is the best tastiness affordable with that much of each, and every fruit is either skipped, bought at full price, or bought at half price for one coupon. Both dimensions are swept downwards so each fruit is used at most once

class Solution(object):
    def maxTastiness(self, price, tastiness, maxAmount, maxCoupons):
        """
        :type price: List[int]
        :type tastiness: List[int]
        :type maxAmount: int
        :type maxCoupons: int
        :rtype: int
        """
        dp = [[0] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        for cost, value in zip(price, tastiness):
            half = cost // 2
            for amount in range(maxAmount, -1, -1):
                row = dp[amount]
                for coupons in range(maxCoupons, -1, -1):
                    best = row[coupons]
                    if cost <= amount:
                        best = max(best, dp[amount - cost][coupons] + value)
                    if coupons and half <= amount:
                        best = max(best, dp[amount - half][coupons - 1] + value)
                    row[coupons] = best
        return dp[maxAmount][maxCoupons]
