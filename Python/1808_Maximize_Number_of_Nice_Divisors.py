# Author: Kaustav Ghosh

class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        if primeFactors <= 3:
            return primeFactors
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
        elif primeFactors % 3 == 1:
            return 4 * pow(3, (primeFactors - 4) // 3, MOD) % MOD
        else:
            return 2 * pow(3, (primeFactors - 2) // 3, MOD) % MOD
