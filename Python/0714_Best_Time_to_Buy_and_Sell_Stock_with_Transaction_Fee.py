# Find max profit buying/selling stock with transaction fee (no simultaneous holds).

# Author: Kaustav Ghosh

class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return cash
