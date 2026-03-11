# Design a max stack with push, pop, top, peekMax, and popMax operations.

# Author: Kaustav Ghosh

class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        self.max_stack.append(max(x, self.max_stack[-1] if self.max_stack else x))

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]

    def popMax(self):
        max_val = self.peekMax()
        buf = []
        while self.top() != max_val:
            buf.append(self.pop())
        self.pop()
        while buf:
            self.push(buf.pop())
        return max_val
