# Author: Kaustav Ghosh
# Problem: Three Divisors
# Approach: Divisors pair up as d against n / d, so the count is even unless one divisor is its own partner, which happens only for a perfect square. A number with exactly three divisors therefore has to be a square, and its divisors must be 1, its root, and itself, which forces the root to have no divisors of its own beyond 1 and itself, that is to be prime. So the test is simply whether n is a perfect square with a prime root; I take the integer square root to avoid floating point entirely, confirm it squares back to n, then trial divide the root up to its own square root.

class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        root = int(n ** 0.5)
        while root * root > n:
            root -= 1
        while (root + 1) * (root + 1) <= n:
            root += 1
        if root * root != n or root < 2:
            return False
        factor = 2
        while factor * factor <= root:
            if root % factor == 0:
                return False
            factor += 1
        return True
