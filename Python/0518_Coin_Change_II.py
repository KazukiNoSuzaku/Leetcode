# You are given coins of different denominations and a total amount of money.
# Return the number of combinations that make up the amount.

# Author: Kaustav Ghosh

class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
