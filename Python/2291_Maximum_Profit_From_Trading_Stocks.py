# Author: Kaustav Ghosh
# Problem: Maximum Profit From Trading Stocks
# Approach: This is a 0/1 knapsack where the budget is total money, each stock's "weight" is its present price and its "value" is the profit (future - present). Only stocks with positive profit are worth considering; dp[b] is the best profit achievable with budget b

class Solution(object):
    def maximumProfit(self, present, future, budget):
        """
        :type present: List[int]
        :type future: List[int]
        :type budget: int
        :rtype: int
        """
        dp = [0] * (budget + 1)
        for cost, sell in zip(present, future):
            profit = sell - cost
            if profit <= 0:
                continue
            for b in range(budget, cost - 1, -1):
                cand = dp[b - cost] + profit
                if cand > dp[b]:
                    dp[b] = cand
        return dp[budget]
