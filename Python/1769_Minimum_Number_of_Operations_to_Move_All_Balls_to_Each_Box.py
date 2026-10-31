# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Move All Balls to Each Box
# Approach: The cost for a box is the sum of distances to every ball, which splits into the balls on its left and the balls on its right, and each part shifts predictably by one step. Moving the target one box to the right adds one operation for every ball already behind it, so the left-hand cost grows by the running count of balls seen so far; the right-hand cost is the mirror image built in a backward pass. Two linear sweeps therefore replace the quadratic pairing of boxes with balls.

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n

        balls = cost = 0
        for index in range(n):
            answer[index] += cost
            balls += boxes[index] == "1"
            cost += balls

        balls = cost = 0
        for index in range(n - 1, -1, -1):
            answer[index] += cost
            balls += boxes[index] == "1"
            cost += balls
        return answer
