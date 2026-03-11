# There are some spherical balloons taped onto a flat wall. The balloons are represented as
# a 2D integer array points where points[i] = [xstart, xend].
# Return the minimum number of arrows that must be shot to burst all balloons.

# Author: Kaustav Ghosh

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for s, e in points[1:]:
            if s > end:
                arrows += 1
                end = e
        return arrows
