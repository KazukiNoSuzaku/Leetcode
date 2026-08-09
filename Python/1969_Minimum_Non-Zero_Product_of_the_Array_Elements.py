# Author: Kaustav Ghosh
# Problem: Minimum Non-Zero Product of the Array Elements
# Approach: Bit swaps preserve each column's count of ones, so we can pair numbers to make them as extreme as possible: keep 2^p-1 whole and form 2^(p-1)-1 pairs each becoming (2^p-2) and 1. The product is (2^p-1) * (2^p-2)^(2^(p-1)-1)

class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        biggest = (1 << p) - 1            # 2^p - 1
        base = (biggest - 1) % MOD        # 2^p - 2
        exponent = (1 << (p - 1)) - 1     # number of paired values
        return (biggest % MOD) * pow(base, exponent, MOD) % MOD
