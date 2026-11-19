# Author: Kaustav Ghosh
# Problem: Minimum Non-Zero Product of the Array Elements
# Approach: A swap of one bit between two elements leaves their sum unchanged, so the whole array keeps a fixed total and the product of a pair with a fixed sum shrinks as the pair is pushed apart. Pairing each value x with its complement 2^p - 1 - x gives a partner for everything except 2^p - 1 itself, and each such pair can be pushed all the way to 1 and 2^p - 2 because together they hold every bit position exactly once. That leaves 2^(p-1) - 1 copies of 2^p - 2, as many ones, and the untouched 2^p - 1, so the product is (2^p - 1) times (2^p - 2) raised to 2^(p-1) - 1. The exponent reaches about 5 * 10^17, so the power is taken with modular exponentiation rather than built up, and the answer is reduced modulo 10^9 + 7 only at the end; p = 1 falls out correctly since the exponent is then zero.

class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        biggest = (1 << p) - 1
        return biggest % MOD * pow(biggest - 1, biggest // 2, MOD) % MOD
