# Author: Kaustav Ghosh
# Problem: 1610 - Maximum Number of Visible Points
# Approach: Sort angles, sliding window of size <= angle; handle points at location separately

import math

class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        angles = []
        at_location = 0

        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            if dx == 0 and dy == 0:
                at_location += 1
            else:
                angles.append(math.degrees(math.atan2(dy, dx)))

        angles.sort()
        # Duplicate to handle circular window
        n = len(angles)
        angles = angles + [a + 360 for a in angles]

        max_visible = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + at_location
