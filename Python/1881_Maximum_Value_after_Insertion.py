# Author: Kaustav Ghosh
# Problem: Maximum Value after Insertion
# Approach: For a positive number insert the digit before the first smaller digit; for a negative number insert before the first larger digit, keeping the magnitude smallest

class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        digit = str(x)
        if n[0] != '-':
            for i, ch in enumerate(n):
                if int(ch) < x:
                    return n[:i] + digit + n[i:]
            return n + digit
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + digit + n[i:]
            return n + digit
