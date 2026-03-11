# Find n-th number divisible by a or b.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7
        lcm = a * b // math.gcd(a, b)
        def count(x): return x // a + x // b - x // lcm
        lo, hi = 1, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n: hi = mid
            else: lo = mid + 1
        return lo % MOD
