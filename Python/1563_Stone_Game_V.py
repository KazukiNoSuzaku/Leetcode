# Author: Kaustav Ghosh
# Problem: 1563 - Stone Game V
# Approach: Interval DP splitting array, recursive with memoization

from functools import lru_cache

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @lru_cache(maxsize=None)
        def dp(l, r):
            if l == r:
                return 0
            total = prefix[r + 1] - prefix[l]
            result = 0
            for mid in range(l, r):
                left_sum = prefix[mid + 1] - prefix[l]
                right_sum = total - left_sum
                if left_sum < right_sum:
                    result = max(result, left_sum + dp(l, mid))
                elif left_sum > right_sum:
                    result = max(result, right_sum + dp(mid + 1, r))
                else:
                    result = max(result, left_sum + dp(l, mid), right_sum + dp(mid + 1, r))
            return result

        return dp(0, n - 1)
