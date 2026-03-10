# We are playing the Guessing Game. The game will work as follows:
# I pick a number between 1 and n. You guess a number. If you guess right, you win the game.
# If you guess wrong, I'll tell you whether the number I picked is higher or lower,
# and you will continue guessing. Every time you guess a wrong number x, you will pay x dollars.
# Given the integer n, return the minimum amount of money you need to guarantee a win
# regardless of what number I pick.

# Example 1:
# Input: n = 10
# Output: 16

# Constraints:
# 1 <= n <= 200

# Author: Kaustav Ghosh

class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for lo in range(1, n - length + 2):
                hi = lo + length - 1
                dp[lo][hi] = float('inf')
                for k in range(lo, hi + 1):
                    cost = k + max(dp[lo][k - 1], dp[k + 1][hi])
                    dp[lo][hi] = min(dp[lo][hi], cost)
        return dp[1][n]
