# Two players take turns removing a perfect square number of stones.
# The player who cannot move loses. Return true if Alice (first player) wins.

# Author: Kaustav Ghosh

class Solution(object):
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]
