# Author: Kaustav Ghosh
# Problem: Maximize Grid Happiness
# Approach: Broken-profile DP over cells, carrying the last n cells (base-3) plus remaining introverts/extroverts; each placement adds base happiness and the two-way adjustment with its up and left neighbors

from functools import lru_cache

class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        MOD = 3 ** n
        TOP = 3 ** (n - 1)

        def interaction(a, b):
            # Change to both people when adjacent (0 means empty, 1 introvert, 2 extrovert)
            if a == 0 or b == 0:
                return 0
            return (-30 if a == 1 else 20) + (-30 if b == 1 else 20)

        @lru_cache(maxsize=None)
        def dp(pos, mask, intro, extro):
            if pos == m * n:
                return 0
            row, col = divmod(pos, n)
            up = mask // TOP                # neighbor n cells back
            left = mask % 3 if col > 0 else 0
            shifted = (mask * 3) % MOD

            best = dp(pos + 1, shifted, intro, extro)  # leave empty

            if intro > 0:
                gain = 120
                if row > 0:
                    gain += interaction(1, up)
                if col > 0:
                    gain += interaction(1, left)
                best = max(best, gain + dp(pos + 1, shifted + 1, intro - 1, extro))

            if extro > 0:
                gain = 40
                if row > 0:
                    gain += interaction(2, up)
                if col > 0:
                    gain += interaction(2, left)
                best = max(best, gain + dp(pos + 1, shifted + 2, intro, extro - 1))

            return best

        return dp(0, 0, introvertsCount, extrovertsCount)
