# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        s = str(x)
        if n[0] == '-':
            # Negative number: insert before first digit that is greater than x
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + s + n[i:]
        else:
            # Positive number: insert before first digit that is smaller than x
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i] + s + n[i:]
        return n + s
