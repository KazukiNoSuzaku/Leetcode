# Author: Kaustav Ghosh
# Problem: Design a Stack With Increment Operation
# Approach: Array stack with lazy increment using auxiliary array

class Solution(object):
    pass

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        val = self.stack.pop() + self.inc[idx]
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]
        self.inc.pop()
        return val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if self.inc:
            idx = min(k, len(self.inc)) - 1
            self.inc[idx] += val
