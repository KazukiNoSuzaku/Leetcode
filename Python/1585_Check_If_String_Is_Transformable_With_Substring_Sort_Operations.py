# Author: Kaustav Ghosh
# Problem: Check If String Is Transformable With Substring Sort Operations
# Approach: Sorting only lets a digit bubble left past larger digits; greedily match each t digit to s's earliest copy, rejecting if a smaller digit blocks it

from collections import deque

class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            positions[int(ch)].append(i)

        for ch in t:
            d = int(ch)
            if not positions[d]:
                return False
            idx = positions[d][0]
            # A smaller digit sitting to the left can't be passed, so d can't reach the front
            if any(positions[k] and positions[k][0] < idx for k in range(d)):
                return False
            positions[d].popleft()
        return True
