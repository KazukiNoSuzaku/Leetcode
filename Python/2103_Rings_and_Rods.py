# Author: Kaustav Ghosh
# https://leetcode.com/problems/rings-and-rods/

class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)
        return sum(1 for s in rods if len(s) == 3)
