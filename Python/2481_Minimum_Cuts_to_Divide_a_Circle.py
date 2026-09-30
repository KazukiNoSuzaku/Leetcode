# Author: Kaustav Ghosh
# Problem: Minimum Cuts to Divide a Circle
# Approach: Every cut is a diameter, so it splits the circle into two pieces at once when the piece count is even, needing n / 2 cuts. For an odd n no cut can be shared, so each of the n slices needs its own cut, and a single piece needs none at all

class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        return n if n % 2 else n // 2
