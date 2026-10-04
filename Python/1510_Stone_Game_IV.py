# Author: Kaustav Ghosh
# Problem: Stone Game IV
# Approach: A position is winning exactly when some square move hands the opponent a losing position, so sweep the counts upward and test the squares that fit. Only the pile size matters, so one boolean per count settles the game

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        winning = [False] * (n + 1)
        for total in range(1, n + 1):
            step = 1
            while step * step <= total:
                if not winning[total - step * step]:
                    winning[total] = True
                    break
                step += 1
        return winning[n]
