# Author: Kaustav Ghosh
# Problem: String Compression II
# Approach: DP with memoization — at each position choose to delete or keep; track last char, its count, and removals left

from functools import lru_cache

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        def run_len(cnt):
            if cnt == 0: return 0
            if cnt == 1: return 1
            if cnt < 10: return 2
            if cnt < 100: return 3
            return 4

        @lru_cache(maxsize=None)
        def dp(i, last, last_cnt, rem):
            if rem < 0:
                return float('inf')
            if i == n:
                return 0
            res = dp(i + 1, last, last_cnt, rem - 1)
            if s[i] == last:
                inc = 1 if last_cnt in (1, 9, 99) else 0
                res = min(res, inc + dp(i + 1, last, last_cnt + 1, rem))
            else:
                res = min(res, 1 + dp(i + 1, s[i], 1, rem))
            return res

        return dp(0, '', 0, k)
