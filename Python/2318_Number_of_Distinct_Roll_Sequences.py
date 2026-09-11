# Author: Kaustav Ghosh
# Problem: Number of Distinct Roll Sequences
# Approach: Count length-n dice sequences where consecutive rolls are coprime and any two rolls within distance 2 differ. DP over (previous roll, roll before that): for each new roll, require gcd(new, prev)==1, new != prev, and new != prev-prev. Sum over valid end states, modulo 1e9+7

from math import gcd
from functools import lru_cache


class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        def dp(pos, prev, prev2):
            if pos == n:
                return 1
            total = 0
            for r in range(1, 7):
                if r == prev or r == prev2:
                    continue
                if prev != 0 and gcd(r, prev) != 1:
                    continue
                total += dp(pos + 1, r, prev)
            return total % MOD

        result = dp(0, 0, 0)
        dp.cache_clear()
        return result
