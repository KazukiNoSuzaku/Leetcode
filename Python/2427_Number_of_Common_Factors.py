# Author: Kaustav Ghosh
# Problem: Number of Common Factors
# Approach: A number divides both a and b exactly when it divides their gcd, so count the divisors of the gcd by testing up to its square root and counting each divisor pair once

from math import gcd, isqrt


class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        g = gcd(a, b)
        count = 0
        for d in range(1, isqrt(g) + 1):
            if g % d == 0:
                count += 1 if d * d == g else 2
        return count
