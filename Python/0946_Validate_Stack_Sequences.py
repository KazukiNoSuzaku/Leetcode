# Check if popped is a valid pop sequence from pushed.

# Author: Kaustav Ghosh

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop(); j += 1
        return not stack
