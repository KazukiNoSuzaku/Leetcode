# Author: Kaustav Ghosh
# Problem: Check If String Is Transformable With Substring Sort Operations
# Approach: Sorting a substring ascending is nothing more than repeatedly swapping an adjacent pair that is out of order, so the only move available is to slide a digit left past a strictly larger one; a digit can therefore never jump over a smaller or equal digit. Reading t left to right, the next occurrence of each digit in s is tracked in a queue, and taking the next d is legal exactly when no digit smaller than d still sits to its left in s, since that smaller digit would block the slide. Failing that check means no sequence of sorts can do it.

from collections import deque


class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        positions = [deque() for _ in range(10)]
        for index, ch in enumerate(s):
            positions[int(ch)].append(index)

        for ch in t:
            digit = int(ch)
            queue = positions[digit]
            if not queue:
                return False
            target = queue[0]
            for smaller in range(digit):
                blocking = positions[smaller]
                if blocking and blocking[0] < target:
                    return False
            queue.popleft()
        return True
