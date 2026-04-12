# Author: Kaustav Ghosh
# Problem: 2300. Successful Pairs of Spells and Potions
# URL: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Difficulty: Medium

import bisect

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
        result = []
        for spell in spells:
            # We need spell * potion >= success
            # potion >= ceil(success / spell)
            # ceil(a/b) = (a + b - 1) // b for positive integers
            min_potion = (success + spell - 1) // spell
            idx = bisect.bisect_left(potions, min_potion)
            result.append(n - idx)
        return result
