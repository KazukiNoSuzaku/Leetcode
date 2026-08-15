# Author: Kaustav Ghosh
# Problem: Stone Game IX
# Approach: Only residues mod 3 matter. Stones divisible by 3 act as parity-flipping skips. With an even count of them, Alice wins exactly when both residue-1 and residue-2 stones exist; with an odd count, she wins only when the two residue classes differ by more than two

from collections import Counter

class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        c = Counter(v % 3 for v in stones)
        c0, c1, c2 = c[0], c[1], c[2]
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        return abs(c1 - c2) > 2
