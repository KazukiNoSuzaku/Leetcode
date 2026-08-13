# Author: Kaustav Ghosh
# Problem: Number of Pairs of Interchangeable Rectangles
# Approach: Two rectangles are interchangeable when they share the same width/height ratio. Use the reduced fraction as a key to avoid float error, count each group, and sum pairs c*(c-1)/2

from collections import Counter
from math import gcd

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        counts = Counter()
        for w, h in rectangles:
            g = gcd(w, h)
            counts[(w // g, h // g)] += 1
        return sum(c * (c - 1) // 2 for c in counts.values())
