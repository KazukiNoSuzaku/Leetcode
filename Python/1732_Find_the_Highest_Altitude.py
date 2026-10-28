# Author: Kaustav Ghosh
# Problem: Find the Highest Altitude
# Approach: The altitude at any point is the running total of the gains so far, so the highest point is the largest value that running total ever takes; the trip starts at zero and that counts as a candidate, which matters when every gain is negative. One pass tracking the total and its maximum is enough, with no need to store the altitudes.

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        highest = 0
        for step in gain:
            altitude += step
            if altitude > highest:
                highest = altitude
        return highest
