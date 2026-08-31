# Author: Kaustav Ghosh
# Problem: Minimum White Tiles After Covering With Carpets
# Approach: DP over position and carpets remaining. At each tile either leave it uncovered (paying 1 if it is white and moving on) or, if a carpet is available, lay one starting here to skip carpetLen tiles at no cost. Memoize on (index, carpets left)

from functools import lru_cache


class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        n = len(floor)

        @lru_cache(maxsize=None)
        def dp(i, k):
            if i >= n:
                return 0
            # option 1: leave tile i uncovered
            best = (1 if floor[i] == '1' else 0) + dp(i + 1, k)
            # option 2: cover starting at i with a carpet
            if k > 0:
                best = min(best, dp(i + carpetLen, k - 1))
            return best

        result = dp(0, numCarpets)
        dp.cache_clear()
        return result
