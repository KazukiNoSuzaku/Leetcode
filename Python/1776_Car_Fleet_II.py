# Author: Kaustav Ghosh

class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        ans = [-1.0] * n
        stack = []  # indices of cars to the right
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack:
                j = stack[-1]
                # Time for car i to reach car j
                if cars[j][1] >= speed:
                    stack.pop()
                else:
                    t = float(pos - cars[j][0]) / (cars[j][1] - speed)
                    if ans[j] < 0 or t <= ans[j]:
                        ans[i] = t
                        break
                    stack.pop()
            stack.append(i)
        return ans
