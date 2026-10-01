# Author: Kaustav Ghosh
# Problem: Maximum Enemy Forts That Can Be Captured
# Approach: An army can only march between a fort of yours and an empty position with nothing but enemy forts in between, so scan the non-zero entries and, whenever two consecutive ones differ, the gap between them is all enemies and counts as a candidate

class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        best = 0
        previous = -1
        for i, value in enumerate(forts):
            if value != 0:
                if previous >= 0 and forts[previous] != value:
                    best = max(best, i - previous - 1)
                previous = i
        return best
