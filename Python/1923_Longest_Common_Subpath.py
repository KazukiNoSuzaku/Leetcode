# Author: Kaustav Ghosh
# https://leetcode.com/problems/longest-common-subpath/

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        # Binary search on length + rolling hash
        MOD = (1 << 61) - 1
        BASE = 131

        def check(length):
            if length == 0:
                return True
            common = None
            for path in paths:
                hashes = set()
                h = 0
                power = pow(BASE, length, MOD)
                for i in range(len(path)):
                    h = (h * BASE + path[i] + 1) % MOD
                    if i >= length:
                        h = (h - (path[i - length] + 1) * power) % MOD
                    if i >= length - 1:
                        hashes.add(h)
                if common is None:
                    common = hashes
                else:
                    common &= hashes
                if not common:
                    return False
            return len(common) > 0

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
