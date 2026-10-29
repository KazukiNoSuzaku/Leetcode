# Author: Kaustav Ghosh
# Problem: Maximum Number of Balls in a Box
# Approach: A ball's box is determined solely by its digit sum, so the whole thing is a tally: walk the range once, add each number's digit sum to a counter, and report the largest count. The digit sum is taken by repeated division rather than by converting to a string, which keeps the inner work to a handful of integer operations.

from collections import Counter


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = Counter()
        for ball in range(lowLimit, highLimit + 1):
            total = 0
            rest = ball
            while rest:
                total += rest % 10
                rest //= 10
            boxes[total] += 1
        return max(boxes.values())
