# Author: Kaustav Ghosh
# Problem: 1553 - Minimum Number of Days to Eat N Oranges
# Approach: BFS/memoized recursion with /2 and /3 shortcuts

from functools import lru_cache

class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(maxsize=None)
        def dp(n):
            if n <= 1:
                return n
            return 1 + min(
                n % 2 + dp(n // 2),
                n % 3 + dp(n // 3)
            )

        return dp(n)
