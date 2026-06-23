# Author: Kaustav Ghosh
# Problem: Stone Game IV
# Approach: DP — dp[i] is True if current player wins with i stones; wins if any square removal leads to a losing state

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
        return dp[n]
