# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times) with the following restriction:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously.

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: Buy on day 1 (price = 1) then sell on day 2 (price = 2) then cooldown.
#              Buy on day 4 (price = 0) then sell on day 5 (price = 2). Total = 3.

# Constraints:
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def maxProfit(self, prices):
        hold = float('-inf')
        sold = 0
        rest = 0
        for p in prices:
            prev_sold = sold
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(rest, prev_sold)
        return max(sold, rest)
