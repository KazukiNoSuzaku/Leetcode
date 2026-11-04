# Author: Kaustav Ghosh
# Problem: Maximize Number of Nice Divisors
# Approach: A nice divisor has to include every distinct prime at least once, so if the primes are used with exponents e1 up to ek then the count of nice divisors is the product of the exponents, and those exponents may sum to at most primeFactors. Maximising a product of positive integers with a fixed sum means splitting into threes, because replacing any part of four or more by a three and the rest never loses and two threes beat three twos. The remainder decides the tail: a leftover of one is better absorbed by turning one three into a four, and a leftover of two simply becomes its own factor. The power is then taken with modular exponentiation since primeFactors reaches a billion.

class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        if primeFactors <= 3:
            return primeFactors
        threes, remainder = divmod(primeFactors, 3)
        if remainder == 0:
            return pow(3, threes, MOD)
        if remainder == 1:
            return pow(3, threes - 1, MOD) * 4 % MOD
        return pow(3, threes, MOD) * 2 % MOD
