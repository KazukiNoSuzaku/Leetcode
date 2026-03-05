# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example:
# Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
#        [[],[-2],[0],[-3],[],[],[],[]]
# Output: [null,null,null,null,-3,null,0,-2]

# Constraints:
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.

# Author: Kaustav Ghosh

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
