# Author: Kaustav Ghosh
# Problem: Design Front Middle Back Queue
# Approach: Two deques split at the middle, rebalanced so 0 <= len(right) - len(left) <= 1; the frontmost-middle rules then map cleanly to left[-1] / right[0]

from collections import deque

class FrontMiddleBackQueue(object):
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.appendleft(val)
        self._balance()

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.append(val)
        self._balance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self._balance()
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()      # even total: frontmost of the two middles
        else:
            val = self.right.popleft()  # odd total: the single middle
        self._balance()
        return val

    def popBack(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        val = self.right.pop() if self.right else self.left.pop()
        self._balance()
        return val
