# Author: Kaustav Ghosh
# Problem 2001: Number of Pairs of Interchangeable Rectangles

from collections import Counter
from math import gcd

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        ratio_count = Counter()
        for w, h in rectangles:
            g = gcd(w, h)
            ratio_count[(w // g, h // g)] += 1
        return sum(c * (c - 1) // 2 for c in ratio_count.values())
