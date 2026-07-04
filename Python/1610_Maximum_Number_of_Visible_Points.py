# Author: Kaustav Ghosh
# Problem: Maximum Number of Visible Points
# Approach: Convert each point to its polar angle, sort, duplicate with +360 for wraparound, then slide a window of size `angle`; points at the location always count

import math

class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        lx, ly = location
        at_location = 0
        angles = []
        for x, y in points:
            if x == lx and y == ly:
                at_location += 1
            else:
                angles.append(math.degrees(math.atan2(y - ly, x - lx)))

        angles.sort()
        angles += [a + 360 for a in angles]

        best = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            best = max(best, right - left + 1)

        return best + at_location
