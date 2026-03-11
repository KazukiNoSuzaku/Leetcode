# Compare two strings after processing backspaces (#).

# Author: Kaustav Ghosh

class Solution(object):
    def backspaceCompare(self, s, t):
        def process(s):
            stack = []
            for c in s:
                if c != '#': stack.append(c)
                elif stack: stack.pop()
            return stack
        return process(s) == process(t)
