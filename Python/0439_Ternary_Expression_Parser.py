# Given a string expression representing arbitrarily nested ternary expressions,
# evaluate the expression and return its result as a string.
# You can always assume that the given expression is valid and only consists of
# digits, '?', ':', 'T', and 'F'.

# Author: Kaustav Ghosh

class Solution(object):
    def parseTernary(self, expression):
        stack = []
        i = len(expression) - 1
        while i >= 0:
            ch = expression[i]
            if stack and stack[-1] == '?':
                stack.pop()  # remove '?'
                true_val = stack.pop()
                stack.pop()  # remove ':'
                false_val = stack.pop()
                stack.append(true_val if ch == 'T' else false_val)
            else:
                stack.append(ch)
            i -= 1
        return stack[0]
