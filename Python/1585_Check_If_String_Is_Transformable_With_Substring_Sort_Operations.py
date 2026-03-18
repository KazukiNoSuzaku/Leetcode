# Author: Kaustav Ghosh
# Problem: 1585 - Check If String Is Transformable With Substring Sort Operations (Premium)
# Approach: Track digit positions, greedily verify each target digit can be moved left

from collections import deque

class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = [deque() for _ in range(10)]
        for i, c in enumerate(s):
            pos[int(c)].appendleft(i)

        for c in t:
            d = int(c)
            if not pos[d]:
                return False
            # The position of d in s
            idx = pos[d][-1]
            # No smaller digit should appear before idx
            for smaller in range(d):
                if pos[smaller] and pos[smaller][-1] < idx:
                    return False
            pos[d].pop()

        return True
