# Author: Kaustav Ghosh

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        highest = 0
        for g in gain:
            current += g
            highest = max(highest, current)
        return highest
