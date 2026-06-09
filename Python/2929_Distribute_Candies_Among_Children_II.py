from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def ways(x):
            return comb(x + 2, 2) if x >= 0 else 0

        return (ways(n)
                - 3 * ways(n - limit - 1)
                + 3 * ways(n - 2 * (limit + 1))
                - ways(n - 3 * (limit + 1)))
