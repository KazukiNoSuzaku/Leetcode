# Author: Kaustav Ghosh
# Problem: Count All Possible Routes
# Approach: Memoized DFS on (city, fuel); a route counts each time we sit at finish, and we keep hopping to any city we can afford

class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(locations)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(city, gas):
            ways = 1 if city == finish else 0
            for nxt in range(n):
                if nxt == city:
                    continue
                cost = abs(locations[city] - locations[nxt])
                if cost <= gas:
                    ways += dp(nxt, gas - cost)
            return ways % MOD

        return dp(start, fuel)
