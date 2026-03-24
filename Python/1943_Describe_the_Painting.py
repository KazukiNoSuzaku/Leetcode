# Author: Kaustav Ghosh
# https://leetcode.com/problems/describe-the-painting/

from collections import defaultdict

class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        events = defaultdict(int)
        for l, r, c in segments:
            events[l] += c
            events[r] -= c
        points = sorted(events.keys())
        result = []
        color_sum = 0
        for i in range(len(points)):
            color_sum += events[points[i]]
            if i + 1 < len(points) and color_sum > 0:
                result.append([points[i], points[i + 1], color_sum])
        return result
