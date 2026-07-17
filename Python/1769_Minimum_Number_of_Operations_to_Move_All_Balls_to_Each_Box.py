# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Move All Balls to Each Box
# Approach: Two sweeps accumulate the cost of pulling balls in from the left and from the right; each box's answer is the sum of both running costs

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        res = [0] * n

        balls = ops = 0
        for i in range(n):
            res[i] += ops
            balls += boxes[i] == '1'
            ops += balls

        balls = ops = 0
        for i in range(n - 1, -1, -1):
            res[i] += ops
            balls += boxes[i] == '1'
            ops += balls

        return res
