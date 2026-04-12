# Author: Kaustav Ghosh
# Problem: 2291. Maximum Profit From Trading Stocks
# URL: https://leetcode.com/problems/maximum-profit-from-trading-stocks/
# Difficulty: Medium
# Premium: True
#
# Approach:
# 0/1 knapsack DP. Budget is the capacity, each stock i has cost present[i]
# and profit max(0, future[i] - present[i]). dp[j] = max profit with budget j.
#
# def maximumProfit(present, future, budget):
#     n = len(present)
#     dp = [0] * (budget + 1)
#     for i in range(n):
#         cost = present[i]
#         profit = future[i] - present[i]
#         if profit <= 0:
#             continue
#         for j in range(budget, cost - 1, -1):
#             dp[j] = max(dp[j], dp[j - cost] + profit)
#     return dp[budget]

class Solution(object):
    pass
