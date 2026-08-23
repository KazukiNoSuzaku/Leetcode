# Author: Kaustav Ghosh
# Problem: Rings and Rods
# Approach: The string is (color, rod) pairs. Record the set of colors on each rod, then count rods holding all three colors

from collections import defaultdict

class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rods = defaultdict(set)
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]
            rods[rod].add(color)
        return sum(1 for colors in rods.values() if len(colors) == 3)
