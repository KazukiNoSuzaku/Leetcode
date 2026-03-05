# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# - MyStack() Initializes the object.
# - void push(int x) Pushes element x to the top of the stack.
# - int pop() Removes the element on the top of the stack and returns that element.
# - int top() Returns the element on the top of the stack.
# - boolean empty() Returns true if the stack is empty, false otherwise.

# Example:
# Input: ["MyStack","push","push","top","pop","empty"]
#        [[],[1],[2],[],[],[]]
# Output: [null,null,null,2,2,false]

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.

# Author: Kaustav Ghosh

from collections import deque

class MyStack(object):
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q
