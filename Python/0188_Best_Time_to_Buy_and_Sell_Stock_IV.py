# You are given an integer array prices where prices[i] is the price of a given stock on the ith day,
# and an integer k. Find the maximum profit you can achieve with at most k transactions.
# Note: You may not engage in multiple transactions simultaneously.

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7

# Constraints:
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
        buy = [float('inf')] * k
        profit = [0] * k
        for price in prices:
            for i in range(k):
                buy[i] = min(buy[i], price - (profit[i-1] if i > 0 else 0))
                profit[i] = max(profit[i], price - buy[i])
        return profit[-1]
