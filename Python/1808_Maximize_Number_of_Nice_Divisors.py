# Author: Kaustav Ghosh
# Problem: Maximize Number of Nice Divisors
# Approach: With prime-factor budget k, the nice-divisor count is the product of the exponents, which is maximized by splitting k into 3s (turning a leftover 1 into 2+2). Fast-exponentiate the result

class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        k = primeFactors
        if k <= 3:
            return k

        threes, remainder = divmod(k, 3)
        if remainder == 0:
            return pow(3, threes, MOD)
        if remainder == 1:
            return pow(3, threes - 1, MOD) * 4 % MOD  # 3+1 -> 2+2
        return pow(3, threes, MOD) * 2 % MOD           # leftover 2
