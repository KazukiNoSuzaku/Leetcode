# Author: Kaustav Ghosh
# Problem: Max Value of Equation
# Approach: Monotone deque tracking max (yj - xj) within window |xi - xj| <= k

from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        dq = deque()  # stores (y - x, x) in decreasing order of y - x
        result = float('-inf')
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()
            if dq:
                result = max(result, y + x + dq[0][0])
            while dq and y - x >= dq[-1][0]:
                dq.pop()
            dq.append((y - x, x))
        return result
