# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0

# Constraints:
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
