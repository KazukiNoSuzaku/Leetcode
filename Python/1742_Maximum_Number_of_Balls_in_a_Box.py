# Author: Kaustav Ghosh
# Problem: Maximum Number of Balls in a Box
# Approach: Each ball lands in the box numbered by its digit sum; tally those and return the fullest box

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
            boxes[sum(int(d) for d in str(ball))] += 1
        return max(boxes.values())
