# Author: Kaustav Ghosh
# Problem: Maximum Score From Removing Stones
# Approach: Every move burns two stones, so the score caps at total//2; it also caps at the two smaller piles combined, since the biggest pile can only ever pair with them

class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = a + b + c
        largest = max(a, b, c)
        return min(total // 2, total - largest)
