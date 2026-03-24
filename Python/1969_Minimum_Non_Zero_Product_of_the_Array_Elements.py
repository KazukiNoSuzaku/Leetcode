# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # Max value is 2^p - 1
        # We pair (2^p - 2) with 1, (2^p - 4) with 3, etc.
        # Result = (2^p - 1) * (2^p - 2)^(2^(p-1) - 1)
        max_val = (1 << p) - 1
        base = max_val - 1
        exp = (1 << (p - 1)) - 1
        return max_val % MOD * pow(base % MOD, exp, MOD) % MOD
