# Author: Kaustav Ghosh
# Problem: Count Special Integers
# Approach: Digit dynamic programming over the decimal form of n, carrying a bitmask of digits already used, whether the prefix still hugs n (tight) and whether any non-zero digit has been placed yet. Leading zeros are not part of the number, so they do not enter the mask, and a completed started number counts as one special integer

from functools import lru_cache


class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(map(int, str(n)))

        @lru_cache(None)
        def count(pos, used, tight, started):
            if pos == len(digits):
                return int(started)
            total = 0
            top = digits[pos] if tight else 9
            for d in range(top + 1):
                if started and used >> d & 1:
                    continue
                if started or d:
                    total += count(pos + 1, used | (1 << d), tight and d == top, True)
                else:
                    total += count(pos + 1, used, tight and d == top, False)
            return total

        result = count(0, 0, True, False)
        count.cache_clear()
        return result
