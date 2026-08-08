# Author: Kaustav Ghosh
# Problem: Three Divisors
# Approach: Count divisors by trial division up to sqrt(n), counting each factor pair. Return true iff there are exactly three (which happens only for squares of primes)

class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                count += 1 if i * i == n else 2
            i += 1
        return count == 3
