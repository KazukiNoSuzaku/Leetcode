# Author: Kaustav Ghosh
# Problem: 1575 - Count All Possible Routes
# Approach: DP with memoization on (city, remaining fuel)

from functools import lru_cache

class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(locations)

        @lru_cache(maxsize=None)
        def dp(city, remaining):
            result = 1 if city == finish else 0
            for next_city in range(n):
                if next_city != city:
                    cost = abs(locations[next_city] - locations[city])
                    if cost <= remaining:
                        result += dp(next_city, remaining - cost)
            return result % MOD

        return dp(start, fuel)
