# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Check if sum of digits raised to power of number of digits equals the number

class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = [int(d) for d in str(n)]
        k = len(digits)
        return sum(d ** k for d in digits) == n
