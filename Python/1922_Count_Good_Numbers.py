# Author: Kaustav Ghosh
# Problem: Count Good Numbers
# Approach: The digits are chosen independently, so the count is a product: each even index takes one of the five even digits and each odd index one of the four single-digit primes. With n digits there are n rounded up over two even indices and n over two odd ones, which makes the answer five to one power times four to the other. Both powers are taken by modular exponentiation, which is what keeps n as large as a quadrillion cheap.

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        evens = (n + 1) // 2
        odds = n // 2
        return pow(5, evens, MOD) * pow(4, odds, MOD) % MOD
