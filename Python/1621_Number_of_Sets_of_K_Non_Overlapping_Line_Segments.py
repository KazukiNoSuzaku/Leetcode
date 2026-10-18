# Author: Kaustav Ghosh
# Problem: Number of Sets of K Non-Overlapping Line Segments
# Approach: The segments may touch at an endpoint but not overlap, so reading left to right the configuration is described by 2k endpoints in which a shared point is used twice; splitting every shared point into two distinct points turns the arrangement into a plain choice of 2k positions out of n + k - 1, and the correspondence is reversible, so the count is exactly that binomial coefficient. Evaluating it needs no table: the numerator and denominator are each a product of at most 2k terms taken modulo the prime, and the division is done by raising the denominator to the power of the modulus minus two.

class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        upper = n + k - 1
        lower = 2 * k
        if lower > upper:
            return 0
        numerator = 1
        for i in range(lower):
            numerator = numerator * (upper - i) % MOD
        denominator = 1
        for i in range(1, lower + 1):
            denominator = denominator * i % MOD
        return numerator * pow(denominator, MOD - 2, MOD) % MOD
