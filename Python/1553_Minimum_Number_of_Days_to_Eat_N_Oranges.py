# Author: Kaustav Ghosh
# Problem: Minimum Number of Days to Eat N Oranges
# Approach: Eating single oranges is only ever worth it to reach a multiple of 2 or 3, so from n the sensible moves are to spend n % 2 days reaching an even count and halve it, or n % 3 days reaching a multiple of three and take two thirds off. Memoising that recursion visits very few states, since each step divides the count

from functools import lru_cache


class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(None)
        def days(remaining):
            if remaining <= 1:
                return remaining
            return 1 + min(remaining % 2 + days(remaining // 2),
                           remaining % 3 + days(remaining // 3))

        result = days(n)
        days.cache_clear()
        return result
