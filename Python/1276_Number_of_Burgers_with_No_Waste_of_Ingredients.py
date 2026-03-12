# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Solve linear equations 4j + 2s = tomatoSlices, j + s = cheeseSlices

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # 4j + 2s = T, j + s = C => j = (T - 2C) / 2, s = C - j
        if (tomatoSlices - 2 * cheeseSlices) % 2 != 0:
            return []
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        if jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
