# Author: Kaustav Ghosh
# Problem: Closest Divisors
# Approach: Find divisors of n+1 and n+2 closest together

import math

class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def closest(n):
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return [1, n]

        a = closest(num + 1)
        b = closest(num + 2)
        if abs(a[0] - a[1]) <= abs(b[0] - b[1]):
            return a
        return b
