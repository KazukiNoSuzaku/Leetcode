# Given an integer n represented as a string, return the smallest good base of n.
# We call k (k >= 2) a good base of n, if all digits of n base k are 1's.
# This means n = 1 + k + k^2 + ... + k^(m-1) for some m >= 2.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        max_m = int(math.log(n, 2)) + 1
        for m in range(max_m, 1, -1):
            # k^m - 1 = n*(k-1) => k ~ n^(1/(m-1))
            k = int(n ** (1.0 / (m - 1)))
            if k >= 2 and (k ** m - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)
