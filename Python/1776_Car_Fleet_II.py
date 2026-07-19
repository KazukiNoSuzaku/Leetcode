# Author: Kaustav Ghosh
# Problem: Car Fleet II
# Approach: Process cars right to left with a monotonic stack of cars ahead. Pop any car ahead that is faster (never caught) or that this car would only reach after it has itself already collided, then the top gives the collision time

class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        answer = [-1.0] * n
        stack = []  # indices of cars ahead, slower-to-faster from top

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack:
                j = stack[-1]
                pj, sj = cars[j]
                if sj >= speed:
                    stack.pop()          # car ahead is faster/equal: never caught
                elif answer[j] > 0 and (pj - pos) / (speed - sj) > answer[j]:
                    stack.pop()          # we'd reach it only after it already collided
                else:
                    break
            if stack:
                j = stack[-1]
                pj, sj = cars[j]
                answer[i] = (pj - pos) / (speed - sj)
            stack.append(i)

        return answer
