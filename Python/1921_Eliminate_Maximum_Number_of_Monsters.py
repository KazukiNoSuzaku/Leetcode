# Author: Kaustav Ghosh
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

import math

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Time for each monster to arrive
        arrival = sorted(math.ceil(float(d) / s) for d, s in zip(dist, speed))
        for i in range(len(arrival)):
            if arrival[i] <= i:
                return i
        return len(arrival)
