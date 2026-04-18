# Author: Kaustav Ghosh
# 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
# Greedy: always fill two largest types, or 1 if only one remains; ans = max(max_val, ceil(total/2))

import math

class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        total = sum(amount)
        max_val = max(amount)
        # If one type dominates, we need max_val seconds (fill it alone each second after pairing)
        # Otherwise we can always pair two types, taking ceil(total/2) seconds
        return max(max_val, (total + 1) // 2)
