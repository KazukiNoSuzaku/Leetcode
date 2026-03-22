# Author: Kaustav Ghosh

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
        return min(total - largest, total // 2)
