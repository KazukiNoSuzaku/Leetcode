# Author: Kaustav Ghosh
# Problem: Maximum Number of Visible Points
# Approach: Rotating the field of view only moves a window over the points' bearings, so I convert each point to its angle from the observer and look for the densest window of the given width. Two details make it work: points sitting exactly on the observer have no bearing at all and are visible from every rotation, so they are counted separately, and the window can straddle the zero direction, which I handle by appending every angle again with 360 added so that the wrap becomes an ordinary stretch of the sorted list. A two-pointer sweep then finds the widest window, with a small tolerance in the comparison because the bearings are floating point and a point exactly on the boundary counts as visible.

from math import atan2, degrees


class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        ox, oy = location
        bearings = []
        at_location = 0
        for x, y in points:
            if x == ox and y == oy:
                at_location += 1
            else:
                bearings.append(degrees(atan2(y - oy, x - ox)))

        bearings.sort()
        distinct = len(bearings)
        bearings += [bearing + 360.0 for bearing in bearings]

        best = 0
        left = 0
        limit = angle + 1e-9
        for right in range(len(bearings)):
            while bearings[right] - bearings[left] > limit:
                left += 1
            window = right - left + 1
            # The duplicated half is only a device for letting a window straddle
            # the zero direction; it must never let one point be counted twice,
            # which a full 360 field of view would otherwise do.
            if window > distinct:
                window = distinct
            if window > best:
                best = window
        return best + at_location
