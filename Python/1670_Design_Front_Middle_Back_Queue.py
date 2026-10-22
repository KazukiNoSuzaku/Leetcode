# Author: Kaustav Ghosh
# Problem: Design Front Middle Back Queue
# Approach: A single list would make middle operations linear, so the queue is split across two deques whose concatenation is the queue, kept balanced so the back half holds either as many elements as the front half or exactly one more. With that invariant the middle is always at a boundary rather than somewhere inside: pushing in the middle appends to the front half, popping the middle takes the last of the front half when the halves are equal and the first of the back half when they are not, which is exactly the rule that the frontmost of two middle positions wins. Every operation is a constant number of deque ends plus a rebalance that moves at most one element.

from collections import deque


class FrontMiddleBackQueue(object):

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _rebalance(self):
        # Invariant: len(back) is len(front) or len(front) + 1.
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.front.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.front.append(val)
        self._rebalance()

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.back.append(val)
        self._rebalance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.back:
            return -1
        value = self.front.popleft() if self.front else self.back.popleft()
        self._rebalance()
        return value

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.back:
            return -1
        value = self.front.pop() if len(self.front) == len(self.back) else self.back.popleft()
        self._rebalance()
        return value

    def popBack(self):
        """
        :rtype: int
        """
        if not self.back:
            return -1
        value = self.back.pop()
        self._rebalance()
        return value


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
