# Author: Kaustav Ghosh
# Problem: Next Greater Numerically Balanced Number
# Approach: A number is balanced when every digit d occurs exactly d times. Scan upward from n+1 and return the first balanced number; the next balanced value is never far away

from collections import Counter

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def balanced(x):
            counts = Counter(str(x))
            return all(int(d) == c for d, c in counts.items())

        x = n + 1
        while not balanced(x):
            x += 1
        return x
