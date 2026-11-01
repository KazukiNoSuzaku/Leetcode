# Author: Kaustav Ghosh
# Problem: Car Fleet II
# Approach: A car can only ever collide with the car directly ahead of it, so the answer for a car depends on what has already been decided for everything to its right, which is why the array is scanned from the back with a stack of cars still able to be hit. A car ahead is discarded when it is at least as fast, since the gap then never closes, and also when the computed meeting time falls after that car has itself crashed and slowed down, because by then it is part of a slower fleet further ahead. Whatever survives on top of the stack gives the collision time directly, and each car is pushed and popped once.

class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        times = [-1.0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            while stack:
                ahead = stack[-1]
                gap = cars[ahead][0] - position
                closing = speed - cars[ahead][1]
                if closing <= 0:
                    stack.pop()
                    continue
                if times[ahead] > 0 and gap >= closing * times[ahead]:
                    stack.pop()
                    continue
                times[i] = float(gap) / closing
                break
            stack.append(i)
        return times
