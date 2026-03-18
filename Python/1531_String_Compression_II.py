# Author: Kaustav Ghosh
# Problem: 1531 - String Compression II (Premium)
# Approach: DP with run-length encoding cost after deletions

from functools import lru_cache

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(i, last, last_count, rem):
            if rem < 0:
                return float('inf')
            if i == n:
                return 0
            # Delete s[i]
            delete = dp(i + 1, last, last_count, rem - 1)
            # Keep s[i]
            if s[i] == last:
                inc = 1 if last_count in (1, 9, 99) else 0
                keep = inc + dp(i + 1, last, last_count + 1, rem)
            else:
                keep = 1 + dp(i + 1, s[i], 1, rem)
            return min(delete, keep)

        return dp(0, '', 0, k)
