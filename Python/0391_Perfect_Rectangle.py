# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an
# axis-aligned rectangle, return true if all the rectangles together form an exact cover
# of a rectangular region.

# Author: Kaustav Ghosh

class Solution(object):
    def isRectangleCover(self, rectangles):
        corners = set()
        area = 0
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        expected = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corners == expected and area == (max_x - min_x) * (max_y - min_y)
