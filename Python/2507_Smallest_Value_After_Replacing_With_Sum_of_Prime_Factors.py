# Author: Kaustav Ghosh
# Problem: Smallest Value After Replacing With Sum of Prime Factors
# Approach: Repeatedly replace n by the sum of its prime factors counted with multiplicity. The sum never exceeds n, so the process settles quickly, and it stops exactly when n maps to itself, which happens for every prime and for 4

class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        while True:
            total = 0
            remaining = n
            factor = 2
            while factor * factor <= remaining:
                while remaining % factor == 0:
                    total += factor
                    remaining //= factor
                factor += 1
            if remaining > 1:
                total += remaining
            if total == n:
                return n
            n = total
