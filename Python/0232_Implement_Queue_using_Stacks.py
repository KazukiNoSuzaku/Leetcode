# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class with amortized O(1) time for each operation.

# Example:
# Input: ["MyQueue","push","push","peek","pop","empty"]
#        [[],[1],[2],[],[],[]]
# Output: [null,null,null,1,1,false]

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.

# Author: Kaustav Ghosh

class MyQueue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
