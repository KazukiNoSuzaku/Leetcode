# Author: Kaustav Ghosh
# https://leetcode.com/problems/design-front-middle-back-queue/

from collections import deque

class FrontMiddleBackQueue(object):
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _balance(self):
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        while len(self.front) < len(self.back) - 1:
            self.front.append(self.back.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.front) < len(self.back):
            self.front.append(val)
        else:
            self.back.appendleft(val)
        # No need to balance since we placed it correctly

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.back.append(val)
        self._balance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        return val

    def popBack(self):
        """
        :rtype: int
        """
        if not self.back:
            return -1
        val = self.back.pop()
        self._balance()
        return val
