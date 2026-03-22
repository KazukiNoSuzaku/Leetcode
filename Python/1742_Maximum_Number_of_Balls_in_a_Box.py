# Author: Kaustav Ghosh

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            s = 0
            n = i
            while n:
                s += n % 10
                n //= 10
            boxes[s] = boxes.get(s, 0) + 1
        return max(boxes.values())
