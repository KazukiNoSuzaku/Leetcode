# Author: Kaustav Ghosh
# Problem: Minimum Number of Days to Eat N Oranges
# Approach: Memoized recursion; the useful moves are halving or thirding, so spend x%2 (or x%3) days reaching a divisible count then divide

from functools import lru_cache

class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(None)
        def dp(x):
            if x <= 1:
                return x
            return 1 + min(x % 2 + dp(x // 2), x % 3 + dp(x // 3))

        return dp(n)
