# Author: Kaustav Ghosh
# Problem: Describe the Painting
# Approach: Sweep line on a difference map of color sums: add the color at a segment start, subtract it at the end. Walk the sorted event points keeping a running sum, emitting each interval between consecutive points whose running sum is positive. Every event point is a real boundary, so pieces are never wrongly merged

class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        delta = {}
        for start, end, color in segments:
            delta[start] = delta.get(start, 0) + color
            delta[end] = delta.get(end, 0) - color

        points = sorted(delta)
        result = []
        run = 0
        prev = points[0]
        run = delta[prev]
        for p in points[1:]:
            if run > 0:
                result.append([prev, p, run])
            run += delta[p]
            prev = p
        return result
