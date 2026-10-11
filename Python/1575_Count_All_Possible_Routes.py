# Author: Kaustav Ghosh
# Problem: Count All Possible Routes
# Approach: A route's future depends only on where you stand and how much fuel is left, never on how you got there, so I count routes by filling a table over (fuel, city): the number of routes from a city with f fuel is one for stopping right there when it is the finish, plus the routes from every other affordable city with the fuel that remains after the hop. Filling the table in increasing order of fuel means every value it reads is already final, so no recursion or memo dictionary is needed.

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
        # Hop costs, precomputed so the main loops stay arithmetic-free.
        costs = [[abs(locations[c] - locations[d]) for d in range(n)] for c in range(n)]

        dp = [[0] * n for _ in range(fuel + 1)]
        for f in range(fuel + 1):
            row = dp[f]
            for c in range(n):
                total = 1 if c == finish else 0
                city_costs = costs[c]
                for d in range(n):
                    if d != c:
                        cost = city_costs[d]
                        if cost <= f:
                            total += dp[f - cost][d]
                row[c] = total % MOD
        return dp[fuel][start]
