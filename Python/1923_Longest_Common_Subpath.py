# Author: Kaustav Ghosh
# Problem: Longest Common Subpath
# Approach: The answer length is monotonic, so binary search it. For a candidate length L, collect the set of double rolling-hash values of every length-L window in the first path and intersect with each other path's window set; L is feasible if some window survives in all paths

import random

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        MOD1, MOD2 = (1 << 61) - 1, (1 << 31) - 1
        B1, B2 = random.randint(256, MOD1 - 1), random.randint(256, MOD2 - 1)

        def window_hashes(path, L):
            h1 = h2 = 0
            p1 = pow(B1, L, MOD1)
            p2 = pow(B2, L, MOD2)
            for i in range(L):
                h1 = (h1 * B1 + path[i] + 1) % MOD1
                h2 = (h2 * B2 + path[i] + 1) % MOD2
            seen = {(h1, h2)}
            for i in range(L, len(path)):
                h1 = (h1 * B1 + path[i] + 1 - p1 * (path[i - L] + 1)) % MOD1
                h2 = (h2 * B2 + path[i] + 1 - p2 * (path[i - L] + 1)) % MOD2
                seen.add((h1, h2))
            return seen

        def feasible(L):
            if L == 0:
                return True
            if any(len(p) < L for p in paths):
                return False
            common = window_hashes(paths[0], L)
            for path in paths[1:]:
                common &= window_hashes(path, L)
                if not common:
                    return False
            return bool(common)

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
