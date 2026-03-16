# Author: Kaustav Ghosh
# Problem: Simplified Fractions
# Approach: Count pairs (num, den) where gcd == 1 and den in 2..n

from math import gcd

class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for den in range(2, n + 1):
            for num in range(1, den):
                if gcd(num, den) == 1:
                    result.append("{}/{}".format(num, den))
        return result
