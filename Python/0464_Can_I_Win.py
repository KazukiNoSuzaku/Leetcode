# In the "100 game" two players take turns adding, to a running total, any integer from 1 to maxChoosable.
# The player that causes the running total to reach or exceed desiredTotal wins.
# Return true if the first player can win, assuming both players play optimally.

# Author: Kaustav Ghosh

class Solution(object):
    def canIWin(self, maxChoosable, desiredTotal):
        if desiredTotal <= 0:
            return True
        if maxChoosable * (maxChoosable + 1) // 2 < desiredTotal:
            return False
        memo = {}

        def can_win(used, total):
            if used in memo:
                return memo[used]
            for i in range(1, maxChoosable + 1):
                if used & (1 << i):
                    continue
                if total + i >= desiredTotal or not can_win(used | (1 << i), total + i):
                    memo[used] = True
                    return True
            memo[used] = False
            return False

        return can_win(0, 0)
