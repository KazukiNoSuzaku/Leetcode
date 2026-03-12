# Author: Kaustav Ghosh
# Binary search with inclusion-exclusion to count numbers divisible by a, b, or c

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        from math import gcd

        def lcm(x, y):
            return x * y // gcd(x, y)

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)

        def count(num):
            return num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc

        lo, hi = 1, 2 * 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
