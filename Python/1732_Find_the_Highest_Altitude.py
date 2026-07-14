# Author: Kaustav Ghosh
# Problem: Find the Highest Altitude
# Approach: Altitudes are the running prefix sums of gain starting at 0; track the maximum along the way

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest
