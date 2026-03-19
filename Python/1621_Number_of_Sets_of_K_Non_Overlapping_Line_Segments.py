# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Combinatorics: C(n + k - 1, 2k)
        MOD = 10 ** 9 + 7

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            if r == 0:
                return 1
            num = 1
            den = 1
            for i in range(r):
                num = num * (n - i) % MOD
                den = den * (i + 1) % MOD
            return num * pow(den, MOD - 2, MOD) % MOD

        return comb(n + k - 1, 2 * k)
