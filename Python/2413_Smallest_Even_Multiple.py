# Author: Kaustav Ghosh
# Problem: Smallest Even Multiple
# Approach: The smallest number divisible by both 2 and n is their least common multiple, which is n when n is already even and 2 * n otherwise

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else 2 * n
