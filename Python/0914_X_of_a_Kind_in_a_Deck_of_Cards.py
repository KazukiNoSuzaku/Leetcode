# Check if a deck of cards can be divided into groups of X identical cards.

# Author: Kaustav Ghosh

import math
from collections import Counter

class Solution(object):
    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()
        g = 0
        for c in counts:
            g = math.gcd(g, c)
        return g >= 2
