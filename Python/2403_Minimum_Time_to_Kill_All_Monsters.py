# Author: Kaustav Ghosh
# Problem: Minimum Time to Kill All Monsters
# Approach: Once k monsters are dead the daily gain is k + 1 whichever ones they were, so killing a monster of power p next costs ceil(p / (k + 1)) days. Only the set of dead monsters matters, so a memoized bitmask search over subsets tries every monster as the next kill

from functools import lru_cache


class Solution(object):
    def minimumTime(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        n = len(power)

        @lru_cache(None)
        def days(mask):
            if mask == (1 << n) - 1:
                return 0
            gain = bin(mask).count('1') + 1
            return min(-(-power[i] // gain) + days(mask | 1 << i)
                       for i in range(n) if not mask >> i & 1)

        result = days(0)
        days.cache_clear()
        return result
