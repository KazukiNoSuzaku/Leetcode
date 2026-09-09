# Author: Kaustav Ghosh
# Problem: Successful Pairs of Spells and Potions
# Approach: Sort potions once. For each spell, a potion succeeds when spell*potion >= success, i.e. potion >= ceil(success/spell). Binary search that threshold in the sorted potions; every potion from there on counts

import bisect
from math import ceil


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n = len(potions)
        res = []
        for spell in spells:
            # smallest potion value p with spell * p >= success
            threshold = -(-success // spell)  # ceil division
            idx = bisect.bisect_left(potions, threshold)
            res.append(n - idx)
        return res
