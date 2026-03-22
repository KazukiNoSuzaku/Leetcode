# Author: Kaustav Ghosh

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fill complete layers first
        total = 0
        floor = 0
        layer = 0
        while total + floor + layer + 1 <= n:
            layer += 1
            floor += layer
            total += floor
        # Now add boxes one by one on the floor
        extra = 0
        while total < n:
            extra += 1
            total += extra
            floor += 1
        return floor
