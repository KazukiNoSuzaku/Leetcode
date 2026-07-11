# Author: Kaustav Ghosh
# Problem: Stone Game VII
# Approach: Interval DP on score difference; the mover takes the sum of what stays after removing an end minus the opponent's best play on the remainder

from functools import lru_cache

class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0
            take_left = (prefix[j + 1] - prefix[i + 1]) - dp(i + 1, j)
            take_right = (prefix[j] - prefix[i]) - dp(i, j - 1)
            return max(take_left, take_right)

        return dp(0, n - 1)
